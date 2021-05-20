# baek12865  
![image](https://user-images.githubusercontent.com/48464681/118960668-7e4ed900-b99e-11eb-850f-08ae19c1a297.png)

   
다이나믹 프로그래밍 연습   
d[i][j] -> i번 째 물건 까지 봤을 때 j 만큼의 무게인 상태에서의 최대 가치   
d[i][j] 는 i 번째 물건을 넣지 못했을 때 d[i-1][j] 와 i번째 물건을 넣었을 때 d[i-1][j-w[i]] + v[i] 중 큰 값을 넣어주는 식으로   
배열을 채워나간다
