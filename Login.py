import asyncio
import time
from pyppeteer.launcher import launch
import random
from retrying import retry  # 设置重试次数用的
from pyquery import PyQuery as pq

async def main(username, pwd, url):
    browser = await launch({'headless': False, 'args': ['--no-sandbox', '--disable-infobars'], }, userDataDir='./userdata',
                           args=['--window-size=1366,768'])
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

    await page.goto(url)
    js1 = '''() =>{
               Object.defineProperties(navigator,{
                 webdriver:{
                   get: () => false
                 }
               })
            }'''

    js2 = '''() => {
            alert (
                window.navigator.webdriver
            )
        }'''

    js3 = '''() => {
            window.navigator.chrome = {
        runtime: {},
        // etc.
      };
        }'''

    js4 = '''() =>{
    Object.defineProperty(navigator, 'languages', {
          get: () => ['en-US', 'en']
        });
            }'''

    js5 = '''() =>{
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5,6],
      });
            }'''

    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)

    # await page.evaluate('''document.getElementById(TPL_username_1).value=""''')
    # await page.type('#TPL_username_1', username, {'delay': input_time_random() - 50})
    await page.type('#TPL_password_1', pwd, {'delay': input_time_random()})

    # await page.screenshot({'path': './headless-test-result.png'})
    time.sleep(2)

    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    if slider:
        print('出现滑块情况判定')
        # await page.screenshot({'path': './headless-login-slide.png'})
        flag = await mouse_slide(page=page)
        if flag:
            # print(page.url)
            # await page.keyboard.press('Enter')
            await page.click('#J_SubmitStatic')
            await get_cookie(page)
            await get_search(page)
    else:
        # await page.keyboard.press('Enter')
        await page.click('#J_SubmitStatic')
        await page.waitFor(20)
        await page.waitForNavigation()
        try:
            global error
            error = await page.Jeval('.error', 'node => node.textContent')
        except Exception as e:
            error = None
            print("登录成功")
        finally:
            if error:
                print('确保账户安全重新输入')
            else:
                await asyncio.sleep(3)
                print(page.url)
                await get_cookie(page)
                # 可继续网页跳转 已经携带 cookie
                try:
                    await get_search(page)
                    # await parse(html)
                except Exception as e:
                    print(e.args)
    # await page_close(browser)

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
        await page.mouse.down()
        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        await page.mouse.up()
    except Exception as e:
        print(e, ':验证失败')
        return None, page
    else:
        await asyncio.sleep(2)
        # 判断是否通过
        slider_again = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
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
    await page.click('button[class="btn-search tb-bg"]')
    # await page.evaluate("""window.scrollTo(0, document.body.scrollHeight)""")
    await asyncio.sleep(5)

    # await page.waitForNavigation()
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

async def parse(html):
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
    res = await page.content()
    # print(res)
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1}; '
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    # 将cookie 放入 cookie 池 以便多次请求 封账号 利用cookie 对搜索内容进行爬取
    file = open('cookies.txt', 'a', encoding='utf-8')
    file.write(cookies)
    return cookies


if __name__ == '__main__':
    username = '落叶成只影成单丶'
    pwd = 'nishishei0723'
    url = "https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9qqVAb1&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(username, pwd, url))