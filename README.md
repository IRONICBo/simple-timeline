# HUST 双创美团俱乐部 讲座Demo

- 日志

```log
asklv@asklvdeMacBook-Pro simple-timeline % docker build -t simple-timeline . --no-cache
[+] Building 615.3s (12/12) FINISHED                                                                                           
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 37B                                                                                       0.0s
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.7                                                             1.9s
 => [1/8] FROM docker.io/library/python:3.7@sha256:53e59319730a41a52e8b3c43bd114131c91ebc8689dcece363b796cb4e623cc1     264.9s
 => => resolve docker.io/library/python:3.7@sha256:53e59319730a41a52e8b3c43bd114131c91ebc8689dcece363b796cb4e623cc1       0.0s
 => => sha256:8e1d92e7d04d2a9a9880cb45dc3c32c2805912cd86abed96d0ada3ff28748205 53.70MB / 53.70MB                        127.5s
 => => sha256:cc9731f4e3bc3680179c10cece663cf0cfe0488918d6795406f4b76f07b787de 10.87MB / 10.87MB                         48.5s
 => => sha256:53e59319730a41a52e8b3c43bd114131c91ebc8689dcece363b796cb4e623cc1 1.86kB / 1.86kB                            0.0s
 => => sha256:8491a634da5f8f5b18682acc9b58dc94ff6efbace472961bb7b94ca0cf229679 9.21kB / 9.21kB                            0.0s
 => => sha256:3a0ac2b0e1189417ece5c0d457849b7998e487bf0e76dc751745596eefbb249c 2.22kB / 2.22kB                            0.0s
 => => sha256:66eadbf427bb41b3e329a95935c65b09c6d3b7a9c2fa8e08417e497df02ed996 5.15MB / 5.15MB                           44.8s
 => => sha256:d337cb12fd7c6fe341850cd38e880f1806d49a65832c9804b06d00f9032382e0 54.68MB / 54.68MB                        192.5s
 => => sha256:a719597fe1ca78e1dc4c43fffc424754228514a791abcb0e0c06302ad022b8ca 189.76MB / 189.76MB                      259.0s
 => => extracting sha256:8e1d92e7d04d2a9a9880cb45dc3c32c2805912cd86abed96d0ada3ff28748205                                 1.3s
 => => sha256:615a38af28944585618687da29a81ab818abc011101dd3c50ef98c17a1c23b80 6.41MB / 6.41MB                          150.6s
 => => extracting sha256:66eadbf427bb41b3e329a95935c65b09c6d3b7a9c2fa8e08417e497df02ed996                                 0.1s
 => => extracting sha256:cc9731f4e3bc3680179c10cece663cf0cfe0488918d6795406f4b76f07b787de                                 0.2s
 => => sha256:eab4e136bce52593ffa87e5b1195398a6dfb8f31ad286fe37d15f8eadbe89625 15.23MB / 15.23MB                        164.7s
 => => sha256:f3da12d7049e3a6908f8bc76e9b643fdcdbaa463ba27dbc02bc9b55ceded2bad 233B / 233B                              166.4s
 => => sha256:f48fe35f6010761df542798db6efe87cafd51fcf00df46b0849afc2f2aa71226 2.89MB / 2.89MB                          175.8s
 => => extracting sha256:d337cb12fd7c6fe341850cd38e880f1806d49a65832c9804b06d00f9032382e0                                 1.5s
 => => extracting sha256:a719597fe1ca78e1dc4c43fffc424754228514a791abcb0e0c06302ad022b8ca                                 4.7s
 => => extracting sha256:615a38af28944585618687da29a81ab818abc011101dd3c50ef98c17a1c23b80                                 0.2s
 => => extracting sha256:eab4e136bce52593ffa87e5b1195398a6dfb8f31ad286fe37d15f8eadbe89625                                 0.4s
 => => extracting sha256:f3da12d7049e3a6908f8bc76e9b643fdcdbaa463ba27dbc02bc9b55ceded2bad                                 0.0s
 => => extracting sha256:f48fe35f6010761df542798db6efe87cafd51fcf00df46b0849afc2f2aa71226                                 0.1s
 => [2/8] WORKDIR /HUST                                                                                                   0.6s
 => [3/8] RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime                                                   0.2s
 => [4/8] WORKDIR /HUST                                                                                                   0.0s
 => [5/8] RUN git clone https://github.91chi.fun/https://github.com/IRONICBo/simple-timeline.git                          3.8s
 => [6/8] WORKDIR /HUST/simple-timeline                                                                                   0.0s
 => [7/8] RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip                                       9.6s
 => [8/8] RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt                               333.5s
 => exporting to image                                                                                                    0.7s
 => => exporting layers                                                                                                   0.7s
 => => writing image sha256:929fb3d45d188313f5cf812724687d3f438ae1e0d8463112fd37e617552593e4                              0.0s
 => => naming to docker.io/library/simple-timeline                                                                        0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

- info

```bash
docker run -p 5001:5000 -p 7001:7000 simple-timeline
```

```bash
apt update # 更新源
apt install vim
```

```bash
flask run -p 7000 -h 0.0.0.0 # 新端口运行
```