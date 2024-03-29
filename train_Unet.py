import sys
import os
from optparse import OptionParser
import numpy as np

import torch
import torch.backends.cudnn as cudnn
import torch.nn as nn
from torch import optim

from eval import eval_net
from unet import UNet
from utils import get_ids, split_ids, split_train_val, get_imgs_and_masks, batch



def train_net(net,
              epochs=30,
              batch_size=6,
              lr=0.1,
              val_percent=0.05,
              save_cp=True,
              gpu=False,
              img_scale=0.5):

#    dir_img = 'E:/A_paper_thesis/paper5/tensorflow_deeplabv3plus_scrapingData/dataset/Scraping_Data2/train_db'
    dir_img = 'data/train_db/'
    dir_mask = 'data/GT_bw/'
    dir_checkpoint = 'checkpoint0919/'

    ids = get_ids(dir_img)
    ids = split_ids(ids)

    iddataset = split_train_val(ids, val_percent)

    print('''
    Starting training:
        Epochs: {}
        Batch size: {}
        Learning rate: {}
        Training size: {}
        Validation size: {}
        Checkpoints: {}
        CUDA: {}
    '''.format(epochs, batch_size, lr, len(iddataset['train']),
               len(iddataset['val']), str(save_cp), str(gpu)))

    N_train = len(iddataset['train'])

    optimizer = optim.SGD(net.parameters(),
                          lr=lr,
                          momentum=0.9,
                          weight_decay=0.0005)

    criterion = nn.BCELoss()
    

    for epoch in range(epochs):
        print('Starting epoch {}/{}.'.format(epoch + 1, epochs))
        net.train()

        # reset the generators
        train = get_imgs_and_masks(iddataset['train'], dir_img, dir_mask, img_scale)
        val = get_imgs_and_masks(iddataset['val'], dir_img, dir_mask, img_scale)

        epoch_loss = 0
        epoch_iou = 0
        epoch_xor=0

        for i, b in enumerate(batch(train, batch_size)):
            imgs = np.array([i[0] for i in b]).astype(np.float32)
            true_masks = np.array([i[1] for i in b])

            imgs = torch.from_numpy(imgs)
            true_masks = torch.from_numpy(true_masks)

            if gpu:
                imgs = imgs.cuda()
                true_masks = true_masks.cuda()

            masks_pred = net(imgs)
            masks_probs_flat = masks_pred.view(-1)

            true_masks_flat = true_masks.view(-1)

            loss = criterion(masks_probs_flat, true_masks_flat)
            epoch_loss += loss.item()
            
            print('step:', i)

#            print('Validation Dice Coeff: {0:.4f} --- loss: {1:.6f}'.format(i * batch_size / N_train, loss.item()))
            print('Validation Dice Coeff: {0:.4f} --- loss: {1:.6f}'.format(i * batch_size / N_train, loss.item()))
            

            
#            # mean iou
#            intersect = sum(masks_probs_flat*true_masks_flat)
#            union = sum(masks_probs_flat+true_masks_flat)
#            iou = (intersect+0.001)/(union-intersect+0.001)
#            epoch_iou +=iou
            
            # mean iou
            smooth = 1e-6 # we smooth to avoid our devision 0/0
            intersect = sum(masks_probs_flat*true_masks_flat)
            union = sum(masks_probs_flat+true_masks_flat)-intersect
            iou = (intersect+smooth)/(union+smooth)
            epoch_iou +=iou
            
            # calculate xor
            # xor quation is: xor = (union(output hợp ground truth) - intersect(output giao ground truth))/ ground truth
            # xor =  (union-intersect)/ground truth
            
            xor = (union - intersect)/sum(true_masks_flat)
            epoch_xor += xor
            


            print('mean IoU: {:.4f}'.format(iou))
#            print('mean IoU1: {:.4f}'.format(iou1))
            print('mean xor: {:.4f}'.format(xor))
            
            # end of mean iou

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print('Epoch finished ! epoch_Loss: {:.6f}'.format(epoch_loss / i))
        print('epoch_iou: {:.4f}'.format(epoch_iou / i))
        print('epoch_xor: {:.4f}'.format(epoch_xor / i))

        if 1:
            val_dice = eval_net(net, val, gpu)
            print('epoch_Validation Dice Coeff: {:.4f}'.format(val_dice))
            # need to write mean iou of evaluate here(reference val_dice)
          

        if save_cp:
            torch.save(net.state_dict(),
                       dir_checkpoint + 'CP{}.pth'.format(epoch + 1))
            print('Checkpoint {} saved !'.format(epoch + 1))
            

def get_args():
    parser = OptionParser()
    parser.add_option('-e', '--epochs', dest='epochs', default=30, type='int',
                      help='number of epochs')
    parser.add_option('-b', '--batch-size', dest='batchsize', default=6,
                      type='int', help='batch size')
    parser.add_option('-l', '--learning-rate', dest='lr', default=0.1,
                      type='float', help='learning rate')
    parser.add_option('-g', '--gpu', action='store_true', dest='gpu',
                      default=False, help='use cuda')
    parser.add_option('-c', '--load', dest='load',
                      default=False, help='load file model')
    parser.add_option('-s', '--scale', dest='scale', type='float',
                      default=0.5, help='downscaling factor of the images')

    (options, args) = parser.parse_args()
    return options

if __name__ == '__main__':
    args = get_args()

    net = UNet(n_channels=3, n_classes=1)

    if args.load:
        net.load_state_dict(torch.load(args.load))
        print('Model loaded from {}'.format(args.load))

    if args.gpu:
        net.cuda()
        # cudnn.benchmark = True # faster convolutions, but more memory

    try:
        train_net(net=net,
                  epochs=args.epochs,
                  batch_size=args.batchsize,
                  lr=args.lr,
                  gpu=args.gpu,
                  img_scale=args.scale)
    except KeyboardInterrupt:
        torch.save(net.state_dict(), 'INTERRUPTED.pth')
        print('Saved interrupt')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
