import torch
import numpy as np

all_num_1 = []
all_num_2 = []
all_ans = []
with open("test.txt", "r") as f:
    for line in f:
       elements = line.split()
       num_1 = float(elements[0])
       num_2 = float(elements[1])
       answer = num_1*num_2

       all_num_1.append(num_1)
       all_num_2.append(num_2)
       all_ans.append(answer)

x1 = np.array(all_num_1)
x2 = np.array(all_num_2)
x = np.append(x1,x2)
x = np.reshape(x, [2, len(x1)])
x = np.transpose(x)
y = np.array(all_ans)

for i in range(len(x1)):
    print(x[i,0],'*',x[i,1],'=',y[i])

x_train = torch.from_numpy(x).float()
y_train = torch.from_numpy(y).float()

model = torch.nn.Sequential(
        torch.nn.Linear(2, 1024),
        torch.nn.ReLU(),
        torch.nn.Linear(1024, 512),
        torch.nn.ReLU(),
        torch.nn.Linear(512, 256),
        torch.nn.ReLU(),
        torch.nn.Linear(256, 1)
        )

criterion = torch.nn.MSELoss(reduction='sum')

optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

for epoch in range(25000):
    output = model(x_train)
    loss = criterion(output, torch.reshape(y_train, (len(x1), 1)))
    print('Epoch: ', epoch, 'Loss: ', loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(output)

torch.save(model,'torch_multiplying_model')