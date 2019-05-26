function Y(aV) {
            function aU(d, c) {
            return d << c | d >>> 32 - c
        }
        function aT(i, h) {
            var n, m, l, k, j;
            return l = 2147483648 & i,
            k = 2147483648 & h,
            n = 1073741824 & i,
            m = 1073741824 & h,
            j = (1073741823 & i) + (1073741823 & h),
            n & m ? 2147483648 ^ j ^ l ^ k : n | m ? 1073741824 & j ? 3221225472 ^ j ^ l ^ k : 1073741824 ^ j ^ l ^ k : j ^ l ^ k
        }
        function aS(e, d, f) {
            return e & d | ~e & f
        }
        function aR(e, d, f) {
            return e & f | d & ~f
        }
        function aQ(e, d, f) {
            return e ^ d ^ f
        }
        function aP(e, d, f) {
            return d ^ (e | ~f)
        }
        function aO(b, n, m, l, k, d, c) {
            return b = aT(b, aT(aT(aS(n, m, l), k), c)),
            aT(aU(b, d), n)
        }
        function aN(b, n, m, l, k, e, c) {
            return b = aT(b, aT(aT(aR(n, m, l), k), c)),
            aT(aU(b, e), n)
        }
        function aM(b, n, m, l, k, f, c) {
            return b = aT(b, aT(aT(aQ(n, m, l), k), c)),
            aT(aU(b, f), n)
        }
        function aL(b, n, m, l, k, g, c) {
            return b = aT(b, aT(aT(aP(n, m, l), k), c)),
            aT(aU(b, g), n)
        }
        function aK(r) {
            for (var q, p = r.length, o = p + 8, n = (o - o % 64) / 64, m = 16 * (n + 1), l = new Array(m - 1), k = 0, j = 0; p > j;) {
                q = (j - j % 4) / 4,
                k = j % 4 * 8,
                l[q] = l[q] | r.charCodeAt(j) << k,
                j++
            }
            return q = (j - j % 4) / 4,
            k = j % 4 * 8,
            l[q] = l[q] | 128 << k,
            l[m - 2] = p << 3,
            l[m - 1] = p >>> 29,
            l
        }
        function aJ(g) {
            var f, j, i = "",
                h = "";
            for (j = 0; 3 >= j; j++) {
                    f = g >>> 8 * j & 255,
                    h = "0" + f.toString(16),
                    i += h.substr(h.length - 2, 2)
                }
            return i
        }
        function aI(f) {
            f = f.replace(/\r\n/g, "\n");
            for (var e = "", h = 0; h < f.length; h++) {
                var g = f.charCodeAt(h);
                128 > g ? e += String.fromCharCode(g) : g > 127 && 2048 > g ? (e += String.fromCharCode(g >> 6 | 192), e += String.fromCharCode(63 & g | 128)) : (e += String.fromCharCode(g >> 12 | 224), e += String.fromCharCode(g >> 6 & 63 | 128), e += String.fromCharCode(63 & g | 128))
            }
            return e
        }
        var aH, aG, aF, aE, aD, aC, aB, aA, az, ay = [],
            ax = 7,
            aw = 12,
            av = 17,
            au = 22,
            at = 5,
            ar = 9,
            aq = 14,
            ap = 20,
            ao = 4,
            an = 11,
            am = 16,
            al = 23,
            ak = 6,
            aj = 10,
            ai = 15,
            ah = 21;
        for (aV = aI(aV), ay = aK(aV), aC = 1732584193, aB = 4023233417, aA = 2562383102, az = 271733878, aH = 0; aH < ay.length; aH += 16) {
                aG = aC,
                aF = aB,
                aE = aA,
                aD = az,
                aC = aO(aC, aB, aA, az, ay[aH + 0], ax, 3614090360),
                az = aO(az, aC, aB, aA, ay[aH + 1], aw, 3905402710),
                aA = aO(aA, az, aC, aB, ay[aH + 2], av, 606105819),
                aB = aO(aB, aA, az, aC, ay[aH + 3], au, 3250441966),
                aC = aO(aC, aB, aA, az, ay[aH + 4], ax, 4118548399),
                az = aO(az, aC, aB, aA, ay[aH + 5], aw, 1200080426),
                aA = aO(aA, az, aC, aB, ay[aH + 6], av, 2821735955),
                aB = aO(aB, aA, az, aC, ay[aH + 7], au, 4249261313),
                aC = aO(aC, aB, aA, az, ay[aH + 8], ax, 1770035416),
                az = aO(az, aC, aB, aA, ay[aH + 9], aw, 2336552879),
                aA = aO(aA, az, aC, aB, ay[aH + 10], av, 4294925233),
                aB = aO(aB, aA, az, aC, ay[aH + 11], au, 2304563134),
                aC = aO(aC, aB, aA, az, ay[aH + 12], ax, 1804603682),
                az = aO(az, aC, aB, aA, ay[aH + 13], aw, 4254626195),
                aA = aO(aA, az, aC, aB, ay[aH + 14], av, 2792965006),
                aB = aO(aB, aA, az, aC, ay[aH + 15], au, 1236535329),
                aC = aN(aC, aB, aA, az, ay[aH + 1], at, 4129170786),
                az = aN(az, aC, aB, aA, ay[aH + 6], ar, 3225465664),
                aA = aN(aA, az, aC, aB, ay[aH + 11], aq, 643717713),
                aB = aN(aB, aA, az, aC, ay[aH + 0], ap, 3921069994),
                aC = aN(aC, aB, aA, az, ay[aH + 5], at, 3593408605),
                az = aN(az, aC, aB, aA, ay[aH + 10], ar, 38016083),
                aA = aN(aA, az, aC, aB, ay[aH + 15], aq, 3634488961),
                aB = aN(aB, aA, az, aC, ay[aH + 4], ap, 3889429448),
                aC = aN(aC, aB, aA, az, ay[aH + 9], at, 568446438),
                az = aN(az, aC, aB, aA, ay[aH + 14], ar, 3275163606),
                aA = aN(aA, az, aC, aB, ay[aH + 3], aq, 4107603335),
                aB = aN(aB, aA, az, aC, ay[aH + 8], ap, 1163531501),
                aC = aN(aC, aB, aA, az, ay[aH + 13], at, 2850285829),
                az = aN(az, aC, aB, aA, ay[aH + 2], ar, 4243563512),
                aA = aN(aA, az, aC, aB, ay[aH + 7], aq, 1735328473),
                aB = aN(aB, aA, az, aC, ay[aH + 12], ap, 2368359562),
                aC = aM(aC, aB, aA, az, ay[aH + 5], ao, 4294588738),
                az = aM(az, aC, aB, aA, ay[aH + 8], an, 2272392833),
                aA = aM(aA, az, aC, aB, ay[aH + 11], am, 1839030562),
                aB = aM(aB, aA, az, aC, ay[aH + 14], al, 4259657740),
                aC = aM(aC, aB, aA, az, ay[aH + 1], ao, 2763975236),
                az = aM(az, aC, aB, aA, ay[aH + 4], an, 1272893353),
                aA = aM(aA, az, aC, aB, ay[aH + 7], am, 4139469664),
                aB = aM(aB, aA, az, aC, ay[aH + 10], al, 3200236656),
                aC = aM(aC, aB, aA, az, ay[aH + 13], ao, 681279174),
                az = aM(az, aC, aB, aA, ay[aH + 0], an, 3936430074),
                aA = aM(aA, az, aC, aB, ay[aH + 3], am, 3572445317),
                aB = aM(aB, aA, az, aC, ay[aH + 6], al, 76029189),
                aC = aM(aC, aB, aA, az, ay[aH + 9], ao, 3654602809),
                az = aM(az, aC, aB, aA, ay[aH + 12], an, 3873151461),
                aA = aM(aA, az, aC, aB, ay[aH + 15], am, 530742520),
                aB = aM(aB, aA, az, aC, ay[aH + 2], al, 3299628645),
                aC = aL(aC, aB, aA, az, ay[aH + 0], ak, 4096336452),
                az = aL(az, aC, aB, aA, ay[aH + 7], aj, 1126891415),
                aA = aL(aA, az, aC, aB, ay[aH + 14], ai, 2878612391),
                aB = aL(aB, aA, az, aC, ay[aH + 5], ah, 4237533241),
                aC = aL(aC, aB, aA, az, ay[aH + 12], ak, 1700485571),
                az = aL(az, aC, aB, aA, ay[aH + 3], aj, 2399980690),
                aA = aL(aA, az, aC, aB, ay[aH + 10], ai, 4293915773),
                aB = aL(aB, aA, az, aC, ay[aH + 1], ah, 2240044497),
                aC = aL(aC, aB, aA, az, ay[aH + 8], ak, 1873313359),
                az = aL(az, aC, aB, aA, ay[aH + 15], aj, 4264355552),
                aA = aL(aA, az, aC, aB, ay[aH + 6], ai, 2734768916),
                aB = aL(aB, aA, az, aC, ay[aH + 13], ah, 1309151649),
                aC = aL(aC, aB, aA, az, ay[aH + 4], ak, 4149444226),
                az = aL(az, aC, aB, aA, ay[aH + 11], aj, 3174756917),
                aA = aL(aA, az, aC, aB, ay[aH + 2], ai, 718787259),
                aB = aL(aB, aA, az, aC, ay[aH + 9], ah, 3951481745),
                aC = aT(aC, aG),
                aB = aT(aB, aF),
                aA = aT(aA, aE),
                az = aT(az, aD)
            }
        var ag = aJ(aC) + aJ(aB) + aJ(aA) + aJ(az);
        return ag.toLowerCase()
    }

//var n = (new Date).getTime()
//var n = '1558842802142'
//var o = '12574478'

//console.log(Y('fcdf50919ff6cc9c93de9eb01b068ed6' + '&' + n + '&' + o + '&' + '{"ut_sk":"1.WpD9nBf3FIIDAIj4YwC4PSBb_21380790_1558837508672.TaoPassword-QQ.shoutaosearch","_xsearchInputQ":"Mac","pos":"3_0","q":"macbook","sourceType":"other","from":"suggest_all-query","_navigation_params":"{&quot;animated&quot;:&quot;0&quot;}","suid":"81EBEE72-488B-4F1A-975E-D6EE59E84FC0","xsearchFromSearchDoor":"true","sugg":"mac_3_0","suggest_rn":"bucketid_24-rn_650fdbc1-5cbc-46ad-879a-35b94d05f247","needTabs":"true","subtype":"text","un":"23cdb6b8b86ee17ac397c9499b014932","share_crt_v":"1","sp_tk":"77 lZ2NvT1lkQ0Rjb2Hvv6U","cpp":"1","shareurl":"true","spm":"a313p.22.206.1035945007068","short_name":"h.e3Ly0Gf","sm":"b394ea","app":"chrome","sst":"1","n":20,"buying":"buyitnow","m":"api4h5","token4h5":"","abtest":"26","wlsort":"26","page":1}'));