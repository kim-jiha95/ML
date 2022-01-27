import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()

# forward 메서드 입니다.
def BN_forward(x, gamma, beta, eps):
    N, D = x.shape
    mu = 1./N * np.sum(x, axis = 0)
    xmu = x - mu
    var = 1./N * np.sum(xmu**2, axis = 0)
    sqrtvar = np.sqrt(var + eps)
    ivar = 1./sqrtvar
    xhat = xmu * ivar
    out = (gamma * xhat) + beta
    values = (xhat,gamma,xmu,ivar,sqrtvar,var,eps)
    return out, values

# Backward 메서드입니다.
def BN_backward(dout, cache):
    # Forward에서 저장해 놓은 값 입력
    xhat,gamma,xmu,ivar,sqrtvar,var,eps = cache
    # 입력의 Shape 저장
    N,D = dout.shape
    
    # (dl/dgamma), (dl/dbeta)를 계산합니다.
    dbeta = np.sum(dout, axis=0)
    dgammax = dout
    dgamma = np.sum(dgammax*xhat, axis=0)
    
    # (dl/dxhat) 를 계산합니다.
    # TODO : 위의 계산한 값을 토대로 dxhat을 만들어주세요.
    dxhat = dgammax * gamma
    
    # (dl/dvar) 를 계산합니다.
    divar = np.sum(dxhat*xmu, axis=0)
    dsqrtvar = -1. /(sqrtvar**2) * divar
    dvar = 0.5 * 1. /np.sqrt(var+eps) * dsqrtvar
    
    # (dl/dmu) 를 계산합니다.
    dxmu1 = dxhat * ivar
    dsq = 1. /N * np.ones((N,D)) * dvar
    dxmu2 = 2 * xmu * dsq
    
    # TODO : 위의 계산한 값을 토대로 dx1을 만들어주세요.
    dx1 = dxmu1 + dxmu2
    
    # (dl/dx) 를 계산합니다.
    dmu = -1 * np.sum(dxmu1+dxmu2, axis=0)
    dx2 = 1. /N * np.ones((N,D)) * dmu
    
    # TODO : 위의 계산한 값을 토대로 dx를 만들어주세요.
    dx = dx1 + dx2
    
    # Update 된 dx, dgamma, dbeta를 반환합니다.
    return dx, dgamma, dbeta

# ReLU Activation Function 메서드입니다.
def ReLU(x):
    return np.maximum(0,x)
    
# 시각화를 위한 메서드입니다.
def histogram(x, title):
    plt.hist(x)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Freqency')
    plt.savefig('plot.png')
    elice_utils.send_image("plot.png")

# 임의의 batch x를 선언합니다.
np.random.seed(50)
x = np.random.rand(50,50)

# BN의 초기 파라미터를 설정합니다.
gamma, beta, epsilon = 1, 0, 10e-7
histogram(x, 'Origin')

# TODO : BN_forward를 수행해주세요.
out, cache = BN_forward(x, gamma, beta, eps)

# TODO : 결과를 ReLU 함수에 넣어주세요.
out = ReLU(out)
histogram(out,'Forward')

# TODO : BN_backward를 수행해주세요.
dx, dgamma, dbeta = BN_forward(out, cache)
histogram(dx, 'Backward')
   
