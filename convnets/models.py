import lasagne
from lasagne import layers
from lasagne.layers import *
from lasagne import nonlinearities
from lasagne.layers.dnn import Conv2DDNNLayer as ConvLayer
from lasagne.updates import nesterov_momentum
from lasagne.updates import adam
from nolearn.lasagne import BatchIterator
from nolearn.lasagne import NeuralNet
import theano
import numpy as np
from lasagne.init import HeNormal
import sys

from EarlyStopping import EarlyStopping
from LearningRateScheduler import LearningRateScheduler
# Add the following line to the nolearn parameter set
# on_epoch_finished=[EarlyStopping(patience=4),]


def float32(k):
    return np.cast['float32'](k)

class AdjustVariable(object):
    def __init__(self, name, start=0.03, stop=0.001):
        self.name = name
        self.start, self.stop = start, stop
        self.ls = None

    def __call__(self, nn, train_history):
        if self.ls is None:
            self.ls = np.linspace(self.start, self.stop, nn.max_epochs)

        epoch = train_history[-1]['epoch']
        new_value = float32(self.ls[epoch - 1])
        getattr(nn, self.name).set_value(new_value)


# for the larger networks (n>=9), we need to adjust pythons recursion limit
sys.setrecursionlimit(10000)


def net0(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net


def net1(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.0005,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net


def net2(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(33,3), pad=(16,1), num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(33,3), pad=(16,1), num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net

def net3(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.0001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net


def net4(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.01,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net

def net5(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, stride=(2,2), filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, stride=(2,2), filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net

def net6(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    num_epochs_train = 60
    base_lr = 0.0001 
    learning_rate_schedule = { 0: base_lr, 7*num_epochs_train/3: base_lr/10, 9*num_epochs_train/10: base_lr/9, }
    

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=base_lr,
        on_epoch_finished=[LearningRateScheduler(learning_rate_schedule),],
        regression=False,
        max_epochs=num_epochs_train,
        verbose=1,
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net

def net7(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.0001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=5),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net

def net8(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = MaxPool2DLayer(layer, pool_size=(2,2))
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    num_epochs_train = 60
    base_lr = 0.0001 
    learning_rate_schedule = { 0: base_lr, 6: base_lr/10, }
    

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=base_lr,
        on_epoch_finished=[LearningRateScheduler(learning_rate_schedule),],
        regression=False,
        max_epochs=num_epochs_train,
        verbose=1,
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net


def net9(n_channels,width,height,n_output=2,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):   
    layer = InputLayer(shape=(None, n_channels, width, height))
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, stride=(2,2), filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, stride=(2,2), filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, filter_size=(3,3), pad=1, num_filters=64)
    layer = dropout(layer,p=0.5)
    layer = Conv2DLayer(layer, nonlinearity=nonlinearity, stride=(2,2), filter_size=(3,3), pad=1, num_filters=64)
    layer = Conv2DLayer(layer, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output)
    layer = GlobalPoolLayer(layer)
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax)

    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=4),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )
    return net

he_norm = HeNormal(gain='relu')
def wideResNet0(n_channels,width,height,n_output=2, n=1, k=1,nonlinearity=nonlinearities.very_leaky_rectify,batch_iterator_train=BatchIterator(batch_size=256),batch_iterator_test=BatchIterator(batch_size=256)):
    '''
    Adapted from https://github.com/Lasagne/Recipes/tree/master/papers/deep_residual_learning.
    Tweaked to be consistent with 'Identity Mappings in Deep Residual Networks', Kaiming He et al. 2016 (https://arxiv.org/abs/1603.05027)
    And 'Wide Residual Networks', Sergey Zagoruyko, Nikos Komodakis 2016 (http://arxiv.org/pdf/1605.07146v1.pdf)
    Depth = 6n + 2
    '''
    #n_filters = {0:16, 1:16*k, 2:32*k, 3:64*k}
    n_filters = {0:64, 1:64, 2:64, 3:64}

    # create a residual learning building block with two stacked 3x3 convlayers as in paper
    def residual_block(l, increase_dim=False, projection=True, first=False, filters=16, nonlinearity=nonlinearities.very_leaky_rectify, prefix='res'):
        if increase_dim:
            first_stride = (2,2)
        else:
            first_stride = (1,1)

        if first:
            # hacky solution to keep layers correct
            bn_pre_relu = l
        else:
            # contains the BN -> ReLU portion, steps 1 to 2
            bn_pre_conv = BatchNormLayer(l,name=prefix+'_bn')
            bn_pre_relu = NonlinearityLayer(bn_pre_conv, nonlinearity,name=prefix+'_nonlin')

        # contains the weight -> BN -> ReLU portion, steps 3 to 5
        conv_1 = batch_norm(ConvLayer(bn_pre_relu, num_filters=filters, filter_size=(3,3), stride=first_stride, nonlinearity=nonlinearity, pad='same', W=he_norm),name=prefix+'_conv1')

        dropout = DropoutLayer(conv_1, p=0.5,name=prefix+'_dropout')

        # contains the last weight portion, step 6
        conv_2 = ConvLayer(dropout, num_filters=filters, filter_size=(3,3), stride=(1,1), nonlinearity=None, pad='same', W=he_norm,name=prefix+'_conv2')

        # add shortcut connections
        if increase_dim:
            # projection shortcut, as option B in paper
            projection = ConvLayer(l, num_filters=filters, filter_size=(1,1), stride=(2,2), nonlinearity=None, pad='same', b=None, name=prefix+'_projection')
            block = ElemwiseSumLayer([conv_2, projection], name=prefix+'_sum')

        elif first:
            # projection shortcut, as option B in paper
            projection = ConvLayer(l, num_filters=filters, filter_size=(1,1), stride=(1,1), nonlinearity=None, pad='same', b=None, name=prefix+'_projection')
            block = ElemwiseSumLayer([conv_2, projection], name=prefix+'_sum')

        else:
            block = ElemwiseSumLayer([conv_2, l], name=prefix+'_sum')

        return block

    # Building the network
    l_in = InputLayer(shape=(None, n_channels, width, height),name='input')


    # first layer, output is 16 x 64 x 64
    l = batch_norm(ConvLayer(l_in, num_filters=n_filters[0], filter_size=(3,3), stride=(1,1), nonlinearity=nonlinearities.rectify, pad='same', W=he_norm),name='batch_norm1')


    # first stack of residual blocks, output is 32 x 64 x 64
    l = residual_block(l, first=True, filters=n_filters[1], prefix='res0_')
    for idx in range(1,n):
        l = residual_block(l, filters=n_filters[1], prefix='res1_'+str(idx))

    # second stack of residual blocks, output is 64 x 32 x 32
    l = residual_block(l, increase_dim=True, filters=n_filters[2], prefix='res3_')
    for idx in range(1,(n+2)):
        l = residual_block(l, filters=n_filters[2], prefix='res4_'+str(idx))


    # third stack of residual blocks, output is 128 x 16 x 16
    l = residual_block(l, increase_dim=True, filters=n_filters[3], prefix='res5_')
    for idx in range(1,(n+2)):
        l = residual_block(l, filters=n_filters[3], prefix='res6_'+str(idx))


    bn_post_conv = BatchNormLayer(l, name='bn_post_conv')
    bn_post_relu = NonlinearityLayer(bn_post_conv, nonlinearity, name='post_conv_nonlin')

    # average pooling
    layer = Conv2DLayer(bn_post_relu, nonlinearity=None, filter_size=(3,3), pad=1, num_filters=n_output, name='last_conv')
    layer = GlobalPoolLayer(layer, name='global_pool')
    layer = NonlinearityLayer(layer,nonlinearity=nonlinearities.softmax, name='softmax')


    net = NeuralNet(
        layer,
        update=adam,
        update_learning_rate=0.001,
        #update_momentum=0.9,
        regression=False,
        max_epochs=100,
        verbose=1,
        on_epoch_finished=[EarlyStopping(patience=5),],
        batch_iterator_train = batch_iterator_train,
        batch_iterator_test = batch_iterator_test,
    )

    return net

