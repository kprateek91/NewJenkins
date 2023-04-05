from fileinput import filename
import fire

def hello(name="World"):
  return "Hello %s!" % name

def determine_file_extension(file_name: str):
  if '.csv' in file_name:
    print(f'{file_name} csv file is detected')
  elif '.sql' in file_name:
    print(f'{file_name} sql file is detected')
  elif '.txt' in file_name:
    print(f'{file_name} text file is detected')
  else:
    print('invalid file, please pass either sql/txt/csv file only')

if __name__ == '__main__':
  fire.Fire(hello)