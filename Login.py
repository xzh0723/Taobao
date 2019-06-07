# 报错：pyppeteer.errors.NetworkError: Protocol Error (Runtime.callFunctionOn): Session closed. Most likely the page has been closed.
# 请前往  https://github.com/miyakogi/pyppeteer/pull/160/files  , 修改pyppeteer源码即可

import asyncio
import time
from pyppeteer.launcher import launch
import random
from retrying import retry  # 设置重试次数用的
from pyquery import PyQuery as pq

async def main(username, pwd, url):
    # 以下使用await 可以针对耗时的操作进行挂起
    # 记：一定要给pyppeteer权限删除用户数据, 即设置userDataDir: 文件夹名称, 否则会报错无法移除用户数据
    browser = await launch({'headless': False, 'args': ['--no-sandbox', '--disable-infobars'], }, userDataDir='./userdata',
                           args=['--window-size=1366,768'])
    page = await browser.newPage()  # 启动新的浏览器页面
    await page.setJavaScriptEnabled(enabled=True)  # 启用js
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    )   # 设置模拟浏览器
    await page.goto(url)
    await page_evaluate(page)  # 修改window.navigator.webdriver = False, 这是绕过淘宝自动化工具检测的关键

    # 使用type选定页面元素，并修改其数值，用于输入账号密码，修改的速度仿人类操作，因为有个输入速度的检测机制
    # 因为 pyppeteer 框架需要转换为js操作，而js和python的类型定义不同，所以写法与参数要用字典，类型导入

    # await page.click('#J_Quick2Static')   # 点击选择密码登录, 看你进入登录页面是否已经是密码登录, 若不是则需要点击选择密码登录, 我这边是一进去就是密码登录

    # 清空用户名输入框, 确保正确输入
    await page.click('.nickx')
    # await page.evaluate('''() => { document.getElementById(TPL_username_1).value="" }''')
    await page.type('#TPL_username_1', username, {'delay': input_time_random() - 50})
    await page.type('#TPL_password_1', pwd, {'delay': input_time_random()})

    # await page.screenshot({'path': './headless-test-result.png'})   # 截图测试
    time.sleep(2)

    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    if slider:
        print('出现滑块情况判定')
        # await page.screenshot({'path': './headless-login-slide.png'})   # 截图测试
        flag = await mouse_slide(page=page)   # js拉动滑块
        if flag:
            # print(page.url)
            # await page.keyboard.press('Enter')  # 模拟按键Enter确定 或鼠标点击登录
            await page.click('#J_SubmitStatic')
            await get_cookie(page)   # 获取cookies
            await get_search(page)   # 跳转搜索
    else:
        # await page.keyboard.press('Enter')
        await page.click('#J_SubmitStatic')
        await page.waitFor(20)
        await page.waitForNavigation()   # 等待跳转
        try:
            global error
            error = await page.Jeval('.error', 'node => node.textContent')   # 检测是否是账号密码错误
        except Exception as e:
            error = None
            print("登录成功")
            print('=============' * 100)
        finally:
            if error:
                print('确保账户安全重新输入')
            else:
                await asyncio.sleep(3)
                print(f'当前页面>> {page.url}')
                print('=============' * 100)
                await get_cookie(page)
                # 可继续网页跳转 已经携带 cookie
                try:
                    await get_search(page)
                    # await parse(html)
                except Exception as e:
                    print(e.args)
    await page_close(browser)

async def page_evaluate(page):
    # 替换淘宝在检测浏览时采集的一些参数。
    # 就是在浏览器运行的时候，始终让window.navigator.webdriver=false
    # navigator是windiw对象的一个属性，同时修改plugins，languages，navigator
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

def retry_if_result_none(result):
    return result is None

async def page_close(browser):

    for _page in await browser.pages():
        await _page.close()
    await browser.close()

@retry(retry_on_result=retry_if_result_none, )
async def mouse_slide(page=None):
    await asyncio.sleep(2)
    try:
        # 鼠标移动到滑块，按下，滑动到头（然后延时处理），松开按键
        await page.hover('#nc_1_n1z')  # 不同场景的验证码模块能名字不同。
        await page.mouse.down()   # 模拟按下鼠标
        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})   # js模拟拖动
        await page.mouse.up()   # 模拟松开鼠标
    except Exception as e:
        print(e, ':验证失败')
        return None, page
    else:
        await asyncio.sleep(2)
        slider_again = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')   # 判断是否通过
        if slider_again != '验证通过':
            return None, page
        else:
            # await page.screenshot({'path': './headless-slide-result.png'}) # 截图测试
            print('验证通过')
            return 1, page

def input_time_random():
    return random.randint(150, 201)

async def get_search(page):
    await page.type('#q', 'Macbook', {'delay': input_time_random()})
    await page.click('button[class="btn-search tb-bg"]')  # 点击搜索商品
    # await page.evaluate('''() =>{ window.scrollTo(0, document.body.scrollHeight) }''')  # 下拉滚动条
    await asyncio.sleep(5)

    html = await page.content()
    # print(html)
    doc = pq(html)
    items = doc('.m-itemlist .items .item').items()
    # 获取商品的图片、价格、成交量和位置等信息
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'location': item.find('.location').text()
        }
        print(product)
        with open('product.txt', 'a', encoding='utf-8') as f:
            f.write(str(product) + '\n')

# 获取登录后cookie
async def get_cookie(page):
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1}; '
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(f'cookies: {cookies}')
    print('=============' * 100)
    # 将cookie 放入 cookie 池 以便多次请求 封账号 利用cookie 对搜索内容进行爬取
    file = open('cookies.txt', 'a', encoding='utf-8')
    file.write(cookies)
    return cookies

if __name__ == '__main__':
    username = '********'   # 修改为自己的用户名
    pwd = '************'   # 修改为自己的密码
    url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9qqVAb1&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(username, pwd, url))
