import pandas as pd

def save(location, cleaness, built_in):
<<<<<<< HEAD
    idx = len(pd.read_csv("database.csv"))
=======
    idx = len(pd.read_csv("P:/자동데이타생성/database1.csv"))
    # E:/Repo_Office/Flask_Ex/project2/database1.csv
>>>>>>> cba5909e2786d7022a1d3415d0e6e289967557d4
    new_df = pd.DataFrame({"location":location,
                           "cleaness":cleaness,
                           "built_in":built_in}, 
                         index = [idx])
<<<<<<< HEAD
    new_df.to_csv("database.csv",mode = "a", header = False)
=======
    new_df.to_csv("P:/자동데이타생성/database1.csv",mode = "a", header = False)
>>>>>>> cba5909e2786d7022a1d3415d0e6e289967557d4
    return None

def load_list():
    house_list = []
<<<<<<< HEAD
    df = pd.read_csv("database.csv")
=======
    df = pd.read_csv("P:/자동데이타생성/database1.csv")
>>>>>>> cba5909e2786d7022a1d3415d0e6e289967557d4
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    # print(house_list)
    return house_list

def now_index():
<<<<<<< HEAD
    df = pd.read_csv("database.csv")
=======
    df = pd.read_csv("P:/자동데이타생성/database1.csv")
>>>>>>> cba5909e2786d7022a1d3415d0e6e289967557d4
    return len(df)-1


def load_house(idx):
<<<<<<< HEAD
    df = pd.read_csv("database.csv")
=======
    df = pd.read_csv("P:/자동데이타생성/database1.csv")
>>>>>>> cba5909e2786d7022a1d3415d0e6e289967557d4
    house_info = df.iloc[idx]
    return house_info

if __name__ =="__main__":
    print(load_list())