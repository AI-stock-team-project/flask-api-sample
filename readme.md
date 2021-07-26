# 개요
Flask Sample Code


# PIP 리스트
(도커 없이 테스트할 때)

`pip install flask`


# flask 실행
(도커 없이 테스트할 때)

`flask run -p 5000`



참고) docker 내에서 이용할 때에는 host 를 `0.0.0.0`으로 주어야 한다. (모든 곳에서 이용가능하게 하겠다는 의미로 보임)
이 설정은 Dockerfile 이나 docker-compose 둘 중 한 군데에서 지정하면 된다. (기본값이 localhost 인 것으로 생각되는데, 
이 경우에 도커 컨테이너에서 실행될 때에 접근이 안 되는 듯함)


# flask 동작 방식에 대한 이해
`flask run`을 하게 되면 `app.py`을 읽는 것으로 보인다. 이 파일에는 '__main__'이 지정되어 있으므로, 이 부분이 
실행이 될 것이다. 반대로 본다면, app.py에 변경이 있고 이를 적용해야 한다면, `flask run`을 다시 해줄 필요가 있다는 
의미로 생각된다. `.py`확장자라는 것은 결과적으로 파이썬 스크립트라는 의미라는 의미이므로. `flask run`은 `app.py`라는 
파이썬 스크립트를 실행해서 띄우고 있다는 의미로 볼 수 있다.

코드가 엄청 많지는 않다. (다른 패키지들과의 의존성은 조금 있지만..)
`flask/cli.py`를 열어서 살펴보면 아래와 같은 부분을 찾을 수 있다.

`flask/cli.py`파일에서 779라인 (flask 2.0.1 기준)
```
@click.command("run", short_help="Run a development server.")
@click.option("--host", "-h", default="127.0.0.1", help="The interface to bind to.")
@click.option("--port", "-p", default=5000, help="The port to bind to.")
```

바로 `app.py`에 대해 찾아보면

`flask/cli.py`파일에서 404라인 (flask 2.0.1 기준)
```
for path in ("wsgi.py", "app.py"):
    import_name = prepare_import(path)
    app = locate_app(self, import_name, None, raise_if_not_found=False)
```
같은 부분을 찾을 수 있다.

결론적으로 말해서, flask 의 시작점은 `wsgi.py` 또는 `app.py`라고 볼 수 있다.


# Docker 실행
`docker-compose up --build --force-recreate -d`

명렁이 실행 후 브라우저에서 다음을 접속

http://localhost:15000