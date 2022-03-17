Git 복제
---

원래 하던 프로젝트를 보완해서 더 좋은 결과물을 만들기 위해 프로젝트를 복사해야하는 상황이 왔다.

그래서 정리를 하게 되었다.

1.mirror 옵션을 이용한 clone

```
git clone --mirror {git 주소}

// 특정 branch만 원한다면 
git clone -b { 브랜치명 } --single-branch --mirror { git repository 주소 }
```

2.repository명.git을 .git으로 이름 변경

```
// clone을 정상적으로 완료했다면 repository명.git 파일이 생성되어 있을 것이다

// 해당 프로젝트.git으로 이동

cd {프로젝트명}.git
```

3.새로운 repository와 연결
```
// .git으로 변경한 디렉토리에서 아래 명령을 실행
git remote set-url origin { 새로운 repository 주소 }
```

4.새 repository에 push
```
// .git으로 변경한 디렉토리에서 아래 명령을 실행
// 아래의 명령을 실행하게 되면 새로운 repository로 push 된다.
git push --mirror
```