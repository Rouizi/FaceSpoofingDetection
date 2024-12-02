# Spoofing Detection State of the Art Review 

This document provides a summarized collection of the most relevant resources on spoofing detection, which will be considered for developing our API.

## Repositories

### FeatherNets\_Face-Anti-spoofing-Attack-Detection-Challenge-CVPR2019

[https://github.com/SoftwareGift/FeatherNets\_Face-Anti-spoofing-Attack-Detection-Challenge-CVPR2019](https://github.com/SoftwareGift/FeatherNets_Face-Anti-spoofing-Attack-Detection-Challenge-CVPR2019)  
License not disclosed, 3rd Place Solution in Face Anti-spoofing Attack Detection Challenge @ CVPR2019, most recent commit 5 years ago, light model, pre trained model weights available, inference is provided in jupyter notebook.

### cvpr2024-face-anti-spoofing-challenge

[https://github.com/xianhua-he/cvpr2024-face-anti-spoofing-challenge](https://github.com/xianhua-he/cvpr2024-face-anti-spoofing-challenge)  
MIT license, 1st place in "Unified Physical-Digital Face Attack Detection" of the 5th Face Anti-spoofing Challenge@CVPR2024, most recent commit 2 months ago, pre-trained model weights available, training and inference scripts available, 50 stars repo

### DGUA\_FAS

[https://github.com/ai-application-and-integration-lab/dgua\_fas](https://github.com/ai-application-and-integration-lab/dgua_fas)  
MIT license, achieves superior performance on domain generalization FAS with known or unknown attacks, most recent commit last year, light model, pretrained model weights available, train and test scripts available, \+20 stars repo

### FAS-SGTD

[https://github.com/clks-wzz/FAS-SGTD](https://github.com/clks-wzz/FAS-SGTD)  
MIT license, achieves state-of-the-art results on five benchmark datasets including OULU-NPU, SiW, CASIAMFSD, Replay-Attack, and the new DMAD, most recent commit 4 years ago, pre trained model weights available, train and test scripts provided.

## Datasets

### nuaaaa

[https://www.kaggle.com/datasets/aleksandrpikul222/nuaaaa](https://www.kaggle.com/datasets/aleksandrpikul222/nuaaaa)  
Apache 2.0 license, training: 1743 real / 12748 fake, testing: 3362 real / 5761 fake, divided into 15 directories real and 15 directories fake, dataset weight 400 MB, 3 upvotes on Kaggle

### Liveness Detection \- Zalo AI Challenge 2022

[https://www.kaggle.com/datasets/hlly34/liveness-detection-zalo-2022](https://www.kaggle.com/datasets/hlly34/liveness-detection-zalo-2022)  
MIT License, 3258 videos and a csv file for labels divided into 4 directories: train (1168), public\_test\_2 (486), public\_test (350), private\_test (1253), each video is a selfie/portrait face with a length of 1-5 seconds, dataset weight 2.82 GB, 8 upvotes on Kaggle

### CelebA-Spoof

[https://github.com/ZhangYuanhan-AI/CelebA-Spoof/tree/master](https://github.com/ZhangYuanhan-AI/CelebA-Spoof/tree/master)  
available for non-commercial research purposes only. Large-scale face anti-spoofing dataset. Contains 625,537 images of 10,177 celebrities captured under different spoof mediums, environments and illumination conditions. Dataset weight 73 GB

## Papers

### Joint Physical-Digital Facial Attack Detection Via Simulating Spoofing Clues

[https://arxiv.org/abs/2404.08450](https://arxiv.org/abs/2404.08450)  
Accepted by CVPRW 2024\. The paper uses 2 types of data augmentation: Simulated Physical Spoofing Clues augmentation (SPSC) and Simulated Digital Spoofing Clues augmentation (SDSC), which significantly improve the capability of the model to detect "unseen" attack types. Won 1 place in "Unified Physical-Digital Face Attack Detection"

### Domain-Generalized Face Anti-Spoofing with Unknown Attacks

[https://arxiv.org/abs/2310.11758](https://arxiv.org/abs/2310.11758)  
18 Oct 2023\. The paper introduce DGUA-FAS, a method designed to enhance face anti-spoofing (FAS) systems against domain-generalized unknown attacks. This approach combines a Transformer-based feature extractor with a Synthetic Unknown Attack Sample Generator (SUASG).

### Deep Spatial Gradient and Temporal Depth Learning for Face Anti-spoofing

[https://arxiv.org/abs/2003.08061](https://arxiv.org/abs/2003.08061)  
Accepted by CVPR2020, proposes a depth-supervised spatio-temporal network for robust face anti-spoofing, introduces novel components like the Residual Spatial Gradient Block, Spatio-Temporal Propagation Module, and a Contrastive Depth Loss is presented for more accurate depth supervision.

## Other resources

Other resources like existing third party apis, surveys, etc. that may be helpful later on when building our anti spoofing api.

### Deep Learning for Face Anti-Spoofing: A Survey

[https://github.com/ZitongYu/DeepFAS](https://github.com/ZitongYu/DeepFAS)  
Comprehensive list of anti spoofing related resources, recently updated.

### Face-Liveness-Detection-SDK-Linux

[https://github.com/FaceOnLive/Face-Liveness-Detection-SDK-Linux](https://github.com/FaceOnLive/Face-Liveness-Detection-SDK-Linux)  
Designed for offline and on-premise use. A demo is available for testing, last commit last month. Can be used for testing and as an example for our API.  
