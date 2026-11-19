import requests


def get_weather(city):
    """查询并打印指定城市的实时天气（接口：wttr.in，无需 key）"""
    url = f"https://wttr.in/{city}?format=j1&lang=zh"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        now = data["current_condition"][0]
        temp = now["temp_C"]
        desc = now["weatherDesc"][0]["value"]
        humidity = now["humidity"]
        wind = now["windspeedKmph"]

        print(f"\n📍 {city}")
        print(f"🌤️  天气：{desc}")
        print(f"🌡️  温度：{temp} ℃")
        print(f"💧 湿度：{humidity} %")
        print(f"💨 风速：{wind} km/h")
    except requests.exceptions.RequestException as e:
        print("网络请求出错：", e)
    except (KeyError, IndexError):
        print("没有查到这个城市，请检查城市名是否正确。")


def main():
    print("===== 天气查询工具（wttr.in）=====")
    while True:
        city = input("\n请输入城市名称（输入 q 退出）：").strip()
        if city.lower() in ("q", "quit", "exit"):
            print("再见！")
            break
        if not city:
            print("城市名不能为空。")
            continue
        get_weather(city)


if __name__ == "__main__":
    main()
