import pandas as pd
from filelock import FileLock


def rm_none(text:str):
    if text == 'None':
        return ''
    else:
        return text

def sync_append(*,csv_filepath:str,values:list, delimeter: str =','):
    df = pd.read_csv(csv_filepath)
    assert len(df.columns) == len(values)
    del df
    values = [f'''"{rm_none(str(i))}"''' for i in values]
    newvalue = str(delimeter.join(values)) + '\n'

    lock_path = f"{csv_filepath}.lock"
    lock = FileLock(lock_path)

    with lock:
        with open(csv_filepath, 'a') as file:
            file.write(newvalue)

if __name__ == '__main__':
    from threading import Thread

    a = Thread(target=sync_append,kwargs=dict(
        csv_filepath='../../high_ground.csv',
        values=[1, 2]
    ))
    b = Thread(target=sync_append,kwargs=dict(
        csv_filepath='../../high_ground.csv',
        values=[3, 7]
    ))

    a.start()
    b.start()

    a.join()
    b.join()
