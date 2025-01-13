import random
import time
import os
import sys

# 問題庫 (100題)
questions = [
    {"question": "太陽系中最大的行星是什麼？", "options": ["地球", "木星", "土星", "火星"], "answer": "木星"},
    {"question": "人類身上最長的骨頭是什麼？", "options": ["手臂骨", "鎖骨", "股骨", "脊椎骨"], "answer": "股骨"},
    {"question": "世界上最長的河流是什麼？", "options": ["長江", "尼羅河", "亞馬遜河", "密西西比河"], "answer": "尼羅河"},
    {"question": "二氧化碳的化學式是什麼？", "options": ["CO", "CO2", "C2O", "C2O2"], "answer": "CO2"},
    {"question": "電的單位是什麼？", "options": ["瓦特", "安培", "伏特", "歐姆"], "answer": "伏特"},
    {"question": "海水為什麼是鹹的？", "options": ["含有鹽分", "溶解氧氣", "溶解礦物質", "含有碳酸鹽"], "answer": "含有鹽分"},
    {"question": "世界上最大的沙漠是什麼？", "options": ["撒哈拉沙漠", "戈壁沙漠", "大維多利亞沙漠", "亞利桑那沙漠"], "answer": "撒哈拉沙漠"},
    {"question": "人體內最多的元素是什麼？", "options": ["碳", "氧", "氫", "鈣"], "answer": "氧"},
    {"question": "北極星位於哪個星座？", "options": ["大熊座", "仙后座", "小熊座", "天琴座"], "answer": "小熊座"},
    {"question": "藍色光波的波長是長還是短？", "options": ["長", "短", "中等", "不可見"], "answer": "短"},
    {"question": "植物進行光合作用的主要部位是什麼？", "options": ["根部", "葉片", "花瓣", "莖部"], "answer": "葉片"},
    {"question": "世界上最深的海溝是什麼？", "options": ["馬里亞納海溝", "湯加海溝", "菲律賓海溝", "日本海溝"], "answer": "馬里亞納海溝"},
    {"question": "血液中的紅血球主要作用是什麼？", "options": ["運輸氧氣", "運輸二氧化碳", "免疫防禦", "凝血"], "answer": "運輸氧氣"},
    {"question": "牛奶中的主要蛋白質是什麼？", "options": ["酪蛋白", "乳糖", "白蛋白", "大豆蛋白"], "answer": "酪蛋白"},
    {"question": "全球最大的島嶼是哪一個？", "options": ["格陵蘭島", "澳大利亞", "馬達加斯加", "新幾內亞"], "answer": "格陵蘭島"},
    {"question": "自然界中的水循環包含哪三個主要過程？", "options": ["蒸發、凝結、降水", "滲透、流動、分解", "蒸發、融化、沉澱", "流動、蒸發、冷卻"], "answer": "蒸發、凝結、降水"},
    {"question": "世界上最大的湖泊是什麼？", "options": ["里海", "密歇根湖", "蘇必利爾湖", "貝加爾湖"], "answer": "里海"},
    {"question": "地球上氧氣主要來自於哪一個過程？", "options": ["光合作用", "火山噴發", "化石燃燒", "水循環"], "answer": "光合作用"},
    {"question": "DNA的全名是什麼？", "options": ["去氧核糖核酸", "核糖核酸", "核苷酸", "氨基酸"], "answer": "去氧核糖核酸"},
    {"question": "黃金的化學符號是什麼？", "options": ["Ag", "Au", "Hg", "Fe"], "answer": "Au"},
    {"question": "人體的正常體溫是多少攝氏度？", "options": ["36°C", "36.5°C", "37°C", "37.5°C"], "answer": "37°C"},
    {"question": "人體內最小的骨頭是什麼？", "options": ["鎚骨", "鐙骨", "砧骨", "耳骨"], "answer": "鐙骨"},
    {"question": "世界上最小的國家是哪一個？", "options": ["梵蒂岡", "摩納哥", "列支敦士登", "聖馬利諾"], "answer": "梵蒂岡"},
    {"question": "維他命C的化學名稱是什麼？", "options": ["抗壞血酸", "核黃素", "維生素B", "生物素"], "answer": "抗壞血酸"},
    {"question": "雪的白色來自於什麼原因？", "options": ["光的折射", "光的散射", "光的吸收", "光的偏振"], "answer": "光的散射"},
    {"question": "鳥類為什麼能飛？", "options": ["羽毛提供推力", "空氣動力學", "骨骼輕盈", "以上皆是"], "answer": "以上皆是"},
    {"question": "世界上最高的山峰是哪一座？", "options": ["珠穆朗瑪峰", "喬戈里峰", "干城章嘉峰", "馬納斯魯峰"], "answer": "珠穆朗瑪峰"},
    {"question": "人體內負責運輸氧氣的細胞是什麼？", "options": ["白血球", "血小板", "紅血球", "神經細胞"], "answer": "紅血球"},
    {"question": "全球面積最大的海洋是哪一個？", "options": ["大西洋", "印度洋", "北冰洋", "太平洋"], "answer": "太平洋"},
    {"question": "光速是多少？", "options": ["300,000 公里/秒", "150,000 公里/秒", "450,000 公里/秒", "600,000 公里/秒"], "answer": "300,000 公里/秒"},
    {"question": "月球上有沒有大氣層？", "options": ["有", "沒有", "部分有", "非常微薄"], "answer": "非常微薄"},
    {"question": "人體內的哪個器官負責解毒？", "options": ["腎臟", "肝臟", "肺臟", "脾臟"], "answer": "肝臟"},
    {"question": "人體的心臟有幾個腔室？", "options": ["2", "3", "4", "6"], "answer": "4"},
    {"question": "化學元素週期表中第1號元素是什麼？", "options": ["氧", "氦", "氫", "碳"], "answer": "氫"},
    {"question": "地球表面有多少百分比被水覆蓋？", "options": ["50%", "60%", "70%", "80%"], "answer": "70%"},
    {"question": "世界上最長的城牆是什麼？", "options": ["萬里長城", "哈德良長城", "柏林牆", "克里米亞長城"], "answer": "萬里長城"},
    {"question": "鉛筆中的芯主要由什麼物質構成？", "options": ["石墨", "鉛", "碳纖維", "石英"], "answer": "石墨"},
    {"question": "人體內的主要能量來源是什麼？", "options": ["蛋白質", "脂肪", "碳水化合物", "維生素"], "answer": "碳水化合物"},
    {"question": "全球面積最小的大陸是哪一個？", "options": ["南極洲", "歐洲", "澳大利亞", "南美洲"], "answer": "澳大利亞"},
    {"question": "蜜蜂主要靠什麼來辨別方向？", "options": ["太陽", "地磁", "氣味", "聲音"], "answer": "太陽"},
    {"question": "世界上最冷的地方是什麼？", "options": ["南極洲", "北極", "格陵蘭", "阿拉斯加"], "answer": "南極洲"},
    {"question": "魚類靠什麼進行呼吸？", "options": ["肺", "鰓", "皮膚", "口腔"], "answer": "鰓"},
    {"question": "世界上最古老的書寫系統是哪一個？", "options": ["楔形文字", "象形文字", "字母系統", "漢字"], "answer": "楔形文字"},
    {"question": "人體的大腦分為哪三個主要部分？", "options": ["大腦、小腦、腦幹", "前腦、中腦、後腦", "左腦、右腦、中腦", "大腦、腦室、腦幹"], "answer": "大腦、小腦、腦幹"},
    {"question": "海豚是魚類還是哺乳類？", "options": ["魚類", "哺乳類", "爬行類", "兩棲類"], "answer": "哺乳類"},
    {"question": "鳥類的羽毛主要由什麼構成？", "options": ["角質蛋白", "膠原蛋白", "肌肉纖維", "脂肪"], "answer": "角質蛋白"},
    {"question": "世界上最大的珊瑚礁是什麼？", "options": ["大堡礁", "紅海珊瑚礁", "馬爾代夫珊瑚礁", "加勒比珊瑚礁"], "answer": "大堡礁"},
    {"question": "化石燃料主要由什麼構成？", "options": ["碳氫化合物", "硫化合物", "氮化合物", "氧化物"], "answer": "碳氫化合物"},
    {"question": "太陽的能量來源是什麼？", "options": ["核融合", "核裂變", "化學反應", "重力壓縮"], "answer": "核融合"},
    {"question": "蚯蚓沒有什麼器官卻能呼吸？", "options": ["肺", "鰓", "氣管", "皮膚"], "answer": "皮膚"},
    {"question": "世界上第一個登上月球的人是誰？", "options": ["尼爾·阿姆斯壯", "尤里·加加林", "巴茲·奧爾德林", "約翰·格倫"], "answer": "尼爾·阿姆斯壯"},
    {"question": "人體內主要儲存脂肪的部位是什麼？", "options": ["肝臟", "脂肪細胞", "肌肉", "血液"], "answer": "脂肪細胞"},
    {"question": "植物的根部主要功能是什麼？", "options": ["吸收水分和養分", "進行光合作用", "保護果實", "排出氧氣"], "answer": "吸收水分和養分"},
    {"question": "世界上最早的印刷術發源於哪個國家？", "options": ["中國", "韓國", "埃及", "德國"], "answer": "中國"},
    {"question": "人體內的血液主要由什麼組成？", "options": ["血漿", "血細胞", "血紅蛋白", "血小板"], "answer": "血漿"},
    {"question": "蚊子吸血時主要尋找人體什麼？", "options": ["汗液", "體溫", "血液中的二氧化碳", "皮膚氣味"], "answer": "血液中的二氧化碳"},
    {"question": "世界上最高的瀑布是什麼？", "options": ["天使瀑布", "尼亞加拉瀑布", "維多利亞瀑布", "伊瓜蘇瀑布"], "answer": "天使瀑布"},
    {"question": "什麼是酸雨？", "options": ["含硫酸和硝酸的雨水", "純淨水的雨水", "含鹽的雨水", "含灰塵的雨水"], "answer": "含硫酸和硝酸的雨水"},
    {"question": "人體的眼睛能分辨多少種顏色？", "options": ["約100萬種", "約700萬種", "約1000萬種", "約500萬種"], "answer": "約700萬種"},
    {"question": "哪一種動物被稱為沙漠之舟？", "options": ["駱駝", "蜥蜴", "蛇", "羚羊"], "answer": "駱駝"},
    {"question": "世界上最快的動物是什麼？", "options": ["獵豹", "遊隼", "劍魚", "兔子"], "answer": "遊隼"},
    {"question": "地球的年齡大約是多少？", "options": ["45億年", "65億年", "25億年", "10億年"], "answer": "45億年"},
    {"question": "植物中的葉綠素是什麼？", "options": ["光合作用的色素", "根部吸收物質", "花朵中的化合物", "果實的養分"], "answer": "光合作用的色素"},
    {"question": "世界上最深的湖泊是哪一個？", "options": ["貝加爾湖", "裡海", "坦干伊喀湖", "密西根湖"], "answer": "貝加爾湖"},
    {"question": "水的沸點是多少攝氏度？", "options": ["100度", "90度", "80度", "110度"], "answer": "100度"},
    {"question": "人體的哪個器官負責分泌胰島素？", "options": ["胰臟", "肝臟", "腎臟", "胃"], "answer": "胰臟"},
    {"question": "世界上第一個人工衛星是什麼？", "options": ["斯普特尼克1號", "阿波羅11號", "航天飛機", "人造月球"], "answer": "斯普特尼克1號"},
    {"question": "人體需要的主要維他命有哪些？", "options": ["A、B、C、D", "K、A、B、C", "E、B、C、D", "A、D、E、K"], "answer": "A、B、C、D"},
    {"question": "動物的主要生殖方式有哪些？", "options": ["卵生和胎生", "孢子生殖和分裂生殖", "無性生殖和分裂生殖", "分裂生殖和胎生"], "answer": "卵生和胎生"},
    {"question": "哪一顆行星被稱為“紅色行星”？", "options": ["火星", "木星", "水星", "金星"], "answer": "火星"},
    {"question": "哪一個元素的符號是O？", "options": ["氧", "金", "氫", "氮"], "answer": "氧"},
    {"question": "人體內的免疫系統主要由哪些組織組成？", "options": ["淋巴系統", "消化系統", "呼吸系統", "神經系統"], "answer": "淋巴系統"},
    {"question": "植物的果實是由什麼部分發育而來的？", "options": ["子房", "花瓣", "葉片", "根部"], "answer": "子房"},
    {"question": "世界上最短的戰爭是什麼？", "options": ["英桑戰爭", "百年戰爭", "三十年戰爭", "克里米亞戰爭"], "answer": "英桑戰爭"},
    {"question": "人體內的神經系統分為哪兩部分？", "options": ["中樞神經和周圍神經", "運動神經和感覺神經", "交感神經和副交感神經", "腦神經和脊神經"], "answer": "中樞神經和周圍神經"},
    {"question": "哪一個國家擁有最多的時間區？", "options": ["俄羅斯", "美國", "中國", "巴西"], "answer": "俄羅斯"},
    {"question": "人體內的主要消化酶有哪些？", "options": ["胃蛋白酶、胰蛋白酶、澱粉酶", "胰蛋白酶、澱粉酶、脂肪酶", "胰島素、澱粉酶、脂肪酶", "胃蛋白酶、胰島素、脂肪酶"], "answer": "胃蛋白酶、胰蛋白酶、澱粉酶"},
    {"question": "地球的自轉會產生什麼現象？", "options": ["晝夜交替", "四季更替", "潮汐現象", "極光現象"], "answer": "晝夜交替"},
    {"question": "蟋蟀是如何發聲的？", "options": ["摩擦翅膀", "摩擦足部", "震動腹部", "鳴叫聲帶"], "answer": "摩擦翅膀"},
    {"question": "世界上最高的自由落體瀑布是什麼？", "options": ["天使瀑布", "伊瓜蘇瀑布", "維多利亞瀑布", "尼亞加拉瀑布"], "answer": "天使瀑布"},
    {"question": "人體內的血型有哪些？", "options": ["A型", "B型", "AB型", "O型"], "answer": "A型, B型, AB型, O型"},
    {"question": "哪一個行星距離地球最近？", "options": ["火星", "金星", "水星", "木星"], "answer": "金星"},
    {"question": "世界上最大的熱帶雨林是什麼？", "options": ["亞馬遜雨林", "剛果雨林", "婆羅洲雨林", "東南亞雨林"], "answer": "亞馬遜雨林"},
    {"question": "人體每天需要多少水分攝取？", "options": ["1升", "2升", "3升", "4升"], "answer": "2升"},
    {"question": "哪一種昆蟲具有最長的壽命？", "options": ["蟬", "螳螂", "甲蟲", "螢火蟲"], "answer": "蟬"},
    {"question": "世界上最早的時鐘是什麼？", "options": ["日晷", "機械鐘", "水鐘", "沙漏"], "answer": "日晷"},
    {"question": "地球上最早的生命形式是什麼？", "options": ["細菌", "藻類", "原核生物", "真菌"], "answer": "原核生物"},
    {"question": "人體的哪個器官負責過濾血液？", "options": ["腎臟", "肝臟", "心臟", "脾臟"], "answer": "腎臟"},
    {"question": "什麼是核分裂？", "options": ["原子核分裂為較小的部分", "兩個原子核融合", "核酸合成", "質子分裂"], "answer": "原子核分裂為較小的部分"},
    {"question": "世界上最小的哺乳動物是什麼？", "options": ["小鼩鼱", "蜂鳥", "蝙蝠", "倭河狸"], "answer": "小鼩鼱"},
    {"question": "植物的種子主要由什麼構成？", "options": ["胚芽", "胚乳", "種皮", "以上皆是"], "answer": "以上皆是"},
    {"question": "海龜是爬行動物還是哺乳動物？", "options": ["爬行動物", "哺乳動物"], "answer": "爬行動物"},
    {"question": "人體內的關節液主要作用是什麼？", "options": ["潤滑關節", "增強骨骼強度", "提供養分", "促進骨骼生長"], "answer": "潤滑關節"},
    {"question": "哪一種動物有最多的心臟？", "options": ["章魚", "鯨魚", "烏賊", "螃蟹"], "answer": "章魚"},
    {"question": "世界上最大的動物是什麼？", "options": ["藍鯨", "大象", "巨型烏賊", "鯨鯊"], "answer": "藍鯨"},
    {"question": "人體的骨骼有多少塊？", "options": ["206塊", "208塊", "210塊", "220塊"], "answer": "206塊"},
    {"question": "什麼是熱帶氣旋？", "options": ["熱帶地區的旋風", "極地的暴風", "溫帶地區的風暴", "山區的颱風"], "answer": "熱帶地區的旋風"},
    {"question": "動物的尾巴有什麼用途？", "options": ["保持平衡", "驅趕昆蟲", "交流", "以上皆是"], "answer": "以上皆是"},
    {"question": "哪一顆行星環繞太陽的軌道最長？", "options": ["天王星", "海王星", "冥王星", "土星"], "answer": "海王星"},
    {"question": "人體的皮膚是身體最大的什麼？", "options": ["器官", "組織", "細胞", "系統"], "answer": "器官"}
]

while len(questions) < 100:
    new_question = {
        "question": f"題目 {len(questions)+1} 是什麼？",
        "options": [f"選項 {i}" for i in range(1, 5)],
        "answer": "選項 1",
    }
    questions.append(new_question)

def shuffle_options(options, answer):
    """隨機排列選項，並保持答案正確"""
    shuffled = options[:]
    random.shuffle(shuffled)
    answer_index = shuffled.index(answer)
    return shuffled, answer_index

def main():
    print("歡迎來到問答遊戲！隨時按下 'q' 結束遊戲。")
    num_questions = random.randint(50, 100)
    selected_questions = random.sample(questions, num_questions)
    
    start_time = time.time()
    score = 0
    
    for i, q in enumerate(selected_questions, start=1):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"第 {i} 題/{num_questions}")
        print(q["question"])
        
        shuffled_options, correct_index = shuffle_options(q["options"], q["answer"])
        for idx, option in enumerate(shuffled_options, start=1):
            print(f"{idx}. {option}")
        
        # 計時
        question_start_time = time.time()
        user_input = input("請輸入答案編號 (或按 'q' 結束遊戲): ")
        question_end_time = time.time()
        
        if user_input.lower() == 'q':
            print("遊戲結束！")
            break
        
        try:
            user_choice = int(user_input)
            if user_choice == correct_index + 1:
                print("答對了！")
                score += 1
            else:
                print(f"答錯了！正確答案是：{q['answer']}")
        except ValueError:
            print("輸入無效，請輸入編號。")
        
        print(f"本題耗時：{question_end_time - question_start_time:.2f} 秒")
        time.sleep(1)

    end_time = time.time()
    print("\n遊戲結束！")
    print(f"總分：{score}/{i}")
    print(f"總耗時：{end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    main()
