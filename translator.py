import pandas as pd

shot_type_translation = {
    "放小球": "net shot",
    "擋小球": "return net",
    "殺球": "smash",
    "點扣": "wrist smash",
    "挑球": "lob",
    "防守回抛": "defensive return lob",
    "長球": "clear",
    "平球": "drive",
    "小平球": "driven flight",
    "後場抽平球": "back-court drive",
    "切球": "drop",
    "過渡切球": "passive drop",
    "推球": "push",
    "撲球": "rush",
    "防守回抽": "defensive return drive",
    "勾球": "cross-court net shot",
    "發短球": "short service",
    "發長球": "long service"
}

df = pd.read_csv("/home/lucia/Documents/GitHub/CoachAI-Projects/ShuttleSet/set/An_Se_Young_Pornpawee_Chochuwong_TOYOTA_THAILAND_OPEN_2021_QuarterFinals/set1.csv")

df["type"] = df["type"].map(shot_type_translation).fillna(df["type"])
df.to_csv("/home/lucia/Documents/GitHub/CoachAI-Projects/ShuttleSet/set/An_Se_Young_Pornpawee_Chochuwong_TOYOTA_THAILAND_OPEN_2021_QuarterFinals/set1.csv", index = False)

