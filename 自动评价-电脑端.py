# -*- coding: gbk -*-
# @Time : 2021/10/23 17:39
import random
import time
import jieba.analyse
import requests
from lxml import etree

jieba.setLogLevel(jieba.logging.INFO)
ck = ''

headers = {
    'cookie': ck,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}


# ��������
def generation(pname, _class=0, _type=1):
    # 0��׷�� 1������
    # class 0������ 1����ȡid
    try:
        name = jieba.analyse.textrank(pname, topK=5, allowPOS='n')[0]
    except:
        name = "����"
    if _class == 1:
        return name
    else:
        datas = {
            1: {
                "��ʼ": [
                    "���������$֮ǰ�����е��Ĺ��ģ���Ϊ�Ҳ�֪��$��������Ʒ����ô�������ǿ������ۺ��Ҿͷ����ˡ�",
                    "�����$֮ǰ�����п����ü��ҵ꣬��󿴵���ҵ�����۲���;�������ҵ��� ",
                    "���˺ü��ҵ꣬Ҳ�Ա��˺ü��ҵ꣬����ֻ�����һ�ҵ�$������á�",
                    "������ȥ�����ѡ������ҡ�",
                    "֮ǰ����ҵ�Ҳ��������������о����������������",
                    "��ҵ�$������̫�����ˣ����˵�һ�ξͻ�������һ�Ρ�"
                ],
                "�м�": [
                    "�յ������ҷǳ��Ŀ��ģ���Ϊ$��������Ʒ����ķǳ��ĺã�",
                    "�𿪰�װ���޵����ˣ����������Ҫ��$!",
                    "��ݳ��죡��װ�ĺܺã�����ϲ��������",
                    "��װ�ĺܾ�����$��������Ʒ�ʷǳ�����",
                    "�յ���ݺ��Ȳ������Ĳ��˰�װ��$������Ƿǳ�ϲ��",
                    "����һ�������Ĺ���Ⱳ��û������ô���õĶ�������"
                ],
                "����": [
                    "������������Ĺ���Ҿ�������´��һ�Ҫ��$�Ļ�����һ����������ҵ���ġ�",
                    "������",
                    "�һ��Ƽ�����$������Ҳ����ҵ�����",
                    "����һ�����Ĺ��",
                    "���ĺ���!�Ժ���$�������ǵ꣡(������)",
                    "��ҿ���������һ�ԣ������̫ˬ�ˣ�һ���϶�������ˬ֮��"
                ]
            },
            0: {
                "��ʼ": [
                    "������ô�õ� $ ,��������ĺ��ã����������һ�ι���ʱʹ�õļ�����",
                    "ʹ���˼��� $ ",
                    "�������򵽵�����õ�$ ",
                    "�Ҳݣ�����ĺ��ð���������������������ǻ�����������ʱ�µ�����һ�̵ļ���!!!!!!!!!",
                    "�Ҳݣ����˼���������$ ��úô�ô��⾫�µ���ۣ���ϸ���Ƥ��������ȥ���������˼�����",
                    "$  ��С�һ����̫���������ˣ����˶�˵�úúúã�",
                    "����˯���ž�����ҵ�� $ ����̫�����ˡ�",
                    "����ţ�ư���һ�첻������һ�죬����һ������һ�꣡"
                ],
                "�м�": [
                    "��������,",
                    "ȷʵ�Ǻö������Ƽ���ҹ���,",
                    "$  ��������ķǳ�����",
                    "$  ����̫�����ˣ����Ǹ������������ı���!!",
                    "$  �̶̼�������飬����һ������",
                    "$  ������ô���ˣ�����������̫�ɰ���",
                    "������Ǹ�С������",
                    "���Ǻ����������ϣ�̫������������"
                ],
                "����": [
                    "�Ƽ����������",
                    "��ҵ���Ҷ���$����������ˢ���������!",
                    "����һ�����Ĺ��",
                    "�Ժ���$������ҵ꣬��û������ô���õĶ�����",
                    "�´λ�����ҵ��� $ ����û������ôţ�ƵĶ���",
                    "�����ܺã����Ӻ�ϲ��",
                    "����˯��������  $  ˯��������̫������",
                    "���������һ�ι���"
                ]
            }
        }
        if _type == 1:
            # return 5, '�����ܺã����Ӻ�ϲ����ÿ�����ϲ��������������ȫ˯���š����ʱ�򿴼������ﶼ˵�þ����ˣ�����������ʱ��ͦ�����ģ�����֮�������ڴ�һ�����ôӿ��Ա�����û������ң���һ�£����ͦ���������ҿͷ�С���Ҳ�ر�ĺã�������ò���ͷ�С���Ҳ������ҵ������أ��������´λ���ع��ա�'
            comments = datas[_type]
            return random.randint(3, 5), (
                    random.choice(comments["��ʼ"]) + random.choice(comments["�м�"]) + random.choice(
                comments["����"])).replace(
                "$", name)
        elif _type == 0:
            comments = datas[_type]
            return (
                    random.choice(comments["��ʼ"]) + random.choice(comments["�м�"]) + random.choice(
                comments["����"])).replace(
                "$", name)


# ��ѯȫ������
def all_evaluate():
    N = {}
    url = 'https://club.jd.com/myJdcomments/myJdcomment.action?'
    req = requests.get(url, headers=headers)
    req_et = etree.HTML(req.text)
    evaluate_data = req_et.xpath('//*[@id="main"]/div[2]/div[1]/div/ul/li')
    # print(evaluate)
    for i, ev in enumerate(evaluate_data):
        na = ev.xpath('a/text()')[0]
        try:
            num = ev.xpath('b/text()')[0]
        except IndexError:
            num = 0
        N[na] = int(num)
    return N


# ��ͨ����
def ordinary(N):
    Order_data = []
    req_et = []
    for i in range((N['�����۶���'] // 20) + 1):
        url = f'https://club.jd.com/myJdcomments/myJdcomment.action?sort=0&page={i + 1}'
        req = requests.get(url, headers=headers)
        req_et.append(etree.HTML(req.text))
    for i in req_et:
        Order_data.extend(i.xpath('//*[@id="main"]/div[2]/div[2]/table/tbody'))
    if len(Order_data) != N['��������']:
        Order_data = []
        for i in req_et:
            Order_data.extend(i.xpath('//*[@id="main"]/div[2]/div[2]/table'))

    print(f"��ǰ����{N['�����۶���']}�����ۡ�")
    for i, Order in enumerate(Order_data):
        oid = Order.xpath('tr[@class="tr-th"]/td/span[3]/a/text()')[0]
        oname = Order.xpath('tr[@class="tr-bd"]/td[1]/div[1]/div[2]/div/a/text()')[0]
        pid = Order.xpath('tr[@class="tr-bd"]/td[1]/div[1]/div[2]/div/a/@href')[0]

        pid = pid.replace('//item.jd.com/', '').replace('.html', '')

        print(f"\t{i}.��ʼ���۶���\t{oname}[{oid}]")
        url2 = f"https://club.jd.com/myJdcomments/saveProductComment.action"
        xing, Str = generation(oname)
        print(f'\t\t��������,�Ǽ�{xing}��', Str)
        data2 = {
            'orderId': oid,
            'productId': pid,  # ��Ʒid
            'score': str(xing),  # ��Ʒ����
            'content': bytes(Str, encoding="gbk"),  # ��������
            'saveStatus': '1',
            'anonymousFlag': '1'
        }
        pj2 = requests.post(url2, headers=headers, data=data2)
        time.sleep(5)
        N['�����۶���'] -= 1
    return N


# ɹ������
def sunbw(N):
    Order_data = []
    for i in range((N['��ɹ��'] // 20) + 1):
        url = f"https://club.jd.com/myJdcomments/myJdcomment.action?sort=1&page={i + 1}"
        req = requests.get(url, headers=headers)
        req_et = etree.HTML(req.text)
        Order_data.extend(req_et.xpath('//*[@id="evalu01"]/div[2]/div[1]/div[@class="comt-plist"]/div[1]'))
    print(f"��ǰ����{N['��ɹ��']}����Ҫɹ����")
    for i, Order in enumerate(Order_data):
        oname = Order.xpath('ul/li[1]/div/div[2]/div[1]/a/text()')[0]
        pid = Order.xpath('@pid')[0]
        oid = Order.xpath('@oid')[0]

        print(f'\t��ʼɹ��{i},{oname}')
        # ��ȡͼƬ
        pname = generation(pname=oname, _class=1)
        url1 = f"https://club.jd.com/discussion/getProductPageImageCommentList.action?productId={pid}"
        imgdata = requests.get(url1, headers=headers).json()
        if imgdata["imgComments"]["imgCommentCount"] == 0:
            url1 = "https://club.jd.com/discussion/getProductPageImageCommentList.action?productId=1190881"
            imgdata = requests.get(url1, headers=headers).json()
        imgurl = imgdata["imgComments"]["imgList"][0]["imageUrl"]

        #
        print(f'\t\tͼƬurl={imgurl}')
        url2 = "https://club.jd.com/myJdcomments/saveShowOrder.action"  # �ύɹ��
        headers['Referer'] = 'https://club.jd.com/myJdcomments/myJdcomment.action?sort=1'
        headers['Origin'] = 'https://club.jd.com'
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'orderId': oid,
            'productId': pid,
            'imgs': imgurl,
            'saveStatus': 3
        }
        req_url2 = requests.post(url2, data={
            'orderId': oid,
            'productId': pid,
            'imgs': imgurl,
            'saveStatus': 3
        }, headers=headers)
        # print(f'\t\t\t{req_url2.text}')
        print('���')
        time.sleep(5)
        N['��ɹ��'] -= 1
    return N


# ׷��
def review(N):
    req_et = []
    Order_data = []
    for i in range((N['��׷��'] // 20) + 1):
        url = f"https://club.jd.com/myJdcomments/myJdcomment.action?sort=3&page={i + 1}"
        req = requests.get(url, headers=headers)
        req_et.append(etree.HTML(req.text))
    for i in req_et:
        Order_data.extend(i.xpath('//*[@id="main"]/div[2]/div[2]/table/tr[@class="tr-bd"]'))
    if len(Order_data) != N['��׷��']:
        Order_data = []
        for i in req_et:
            Order_data.extend(i.xpath('//*[@id="main"]/div[2]/div[2]/table/tbody/tr[@class="tr-bd"]'))

    print(f"��ǰ����{N['��׷��']}����Ҫ׷����")
    for i, Order in enumerate(Order_data):
        oname = Order.xpath('td[1]/div/div[2]/div/a/text()')[0]
        _id = Order.xpath('td[3]/div/a/@href')[0]
        # date = Order.xpath('td[2]/div/text()')[0]
        print(f'\t��ʼ��{i}��{oname}')
        url1 = "https://club.jd.com/afterComments/saveAfterCommentAndShowOrder.action"
        pid, oid = _id.replace('http://club.jd.com/afterComments/productPublish.action?sku=', "").split('&orderId=')
        context = generation(oname, _type=0)
        print(f'\t\t׷�����ݣ�{context}')
        req_url1 = requests.post(url1, headers=headers, data={
            'orderId': oid,
            'productId': pid,
            'content': bytes(context, encoding="gbk"),
            'anonymousFlag': 1,
            'score': 5
        })
        # print(f'\t\t\tr{req_url1.text}')
        print('���')
        time.sleep(5)
        N['��׷��'] -= 1
    return N


# ��������
def Service_rating(N):
    Order_data = []
    req_et = []
    for i in range((N['��������'] // 20) + 1):
        url = f"https://club.jd.com/myJdcomments/myJdcomment.action?sort=4&page={i + 1}"
        req = requests.get(url, headers=headers)
        req_et.append(etree.HTML(req.text))
    for i in req_et:
        Order_data.extend(i.xpath('//*[@id="main"]/div[2]/div[2]/table/tbody/tr[@class="tr-bd"]'))
    if len(Order_data) != N['��������']:
        Order_data = []
        for i in req_et:
            Order_data.extend(i.xpath('//*[@id="main"]/div[2]/div[2]/table/tr[@class="tr-bd"]'))
    print(f"��ǰ����{N['��������']}����Ҫ�������ۡ�")
    for i, Order in enumerate(Order_data):
        oname = Order.xpath('td[1]/div[1]/div[2]/div/a/text()')[0]
        oid = Order.xpath('td[4]/div/a[1]/@oid')[0]
        print(f'\t��ʼ��{i}��{oname}')
        url1 = f'https://club.jd.com/myJdcomments/insertRestSurvey.action?voteid=145&ruleid={oid}'
        data1 = {
            'oid': oid,
            'gid': '32',
            'sid': '186194',
            'stid': '0',
            'tags': '',
            'ro591': f'591A{random.randint(3, 5)}',  # ��Ʒ���϶�
            'ro592': f'592A{random.randint(3, 5)}',  # ��ҷ���̬��
            'ro593': f'593A{random.randint(3, 5)}',  # ��������ٶ�
            'ro899': f'899A{random.randint(3, 5)}',  # ���Ա����
            'ro900': f'900A{random.randint(3, 5)}'  # ���Ա����
        }
        pj1 = requests.post(url1, headers=headers, data=data1)
        print("\t\t", pj1.text)
        time.sleep(5)
        N['��������'] -= 1
    return N


def No():
    print()
    N = all_evaluate()
    for i in N:
        print(i, N[i], end="----")
    print()
    return N


def main():
    print("��ʼ�����������ۣ�\n")
    N = No()
    if not N:
        print('Ck���ִ���������ץȡ��')
        exit()
    if N['�����۶���'] != 0:
        print("1.��ʼ��ͨ����")
        N = ordinary(N)
        N = No()
    if N['��ɹ��'] != 0:
        print("2.��ʼɹ������")
        N = sunbw(N)
        N = No()
    if N['��׷��'] != 0:
        print("3.��ʼ����׷����")
        N = review(N)
        N = No()
    if N['��������'] != 0:
        print('4.��ʼ��������')
        N = Service_rating(N)
        N = No()
    print("ȫ���������")


if __name__ == '__main__':
    main()
