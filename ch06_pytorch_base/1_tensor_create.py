import torch
import numpy as np

print("创建一个数")
tensor1 = torch.tensor(10.0)
print(tensor1)
print(tensor1.shape)
print(tensor1.dtype)

print("创建一维向量")
tensor2 = torch.tensor([1,2,3])
print(tensor2)
print(tensor2.shape)
print(tensor2.dtype)

print("创建二维")
tensor3 = torch.tensor(np.array([[1,2,3],[4,5,6]]))
print(tensor3)
print(tensor3.shape)
print(tensor3.dtype)

print("Tensor指定形状（默认float32）")
tensor4 = torch.Tensor(2,3,4)
print(tensor4)
print(tensor4.shape)
print(tensor4.dtype)

# 小写tensor只能传内容；大写Tensor能传形状，默认float32