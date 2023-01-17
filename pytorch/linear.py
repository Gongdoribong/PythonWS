import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)    #결과 고정

x_train = torch.FloatTensor([[1],[2],[3]])
y_train = torch.FloatTensor([[2],[4],[6]])

W = torch.zeros(1, requires_grad=True)  #가중치 W를 0으로 초기화하고 변수 명시
b = torch.zeros(1, requires_grad=True)  #편향

hypothesis = x_train * W + b    #가설 설정 (직선), grad_fn=<AddBackward0>

#현 상태 : y = 0*x + 0

cost = torch.mean((hypothesis - y_train)**2)    #평균 제곱 오차 선언

optimizer = optim.SGD([W, b], lr=0.01)  #SGD:경사하강법, lr:학습률

optimizer.zero_grad()   #gradient를 0으로 초기화

cost.backward() #비용 함수를 미분하여 gradient 계산

optimizer.step()    #W와 b를 업데이트