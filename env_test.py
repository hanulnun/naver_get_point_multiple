import os


if __name__ == "__main__":
  

  print("환경변수 가져오기")
  a = os.environ.get("NAVER_TEST_ENV_VALUE")
  print(a)
  print("환경변수 저장하기")
  env_file = os.getenv('GITHUB_ENV')
  with open(env_file, "a") as myfile:
    myfile.write("NAVER_TEST_ENV_VALUE=N")
  
  # os.system(f'echo \'NAVER_TEST_ENV_VALUE=N\' >> $GITHUB_ENV')