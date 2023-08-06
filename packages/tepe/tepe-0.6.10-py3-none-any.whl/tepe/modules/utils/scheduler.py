import math
from functools import partial
from torch.optim.lr_scheduler import _LRScheduler


class PolyLR(_LRScheduler):
    def __init__(self, optimizer, max_iters, power=0.9, last_epoch=-1, min_lr=1e-6):
        self.power = power
        self.max_iters = max_iters  # avoid zero lr
        self.min_lr = min_lr
        super(PolyLR, self).__init__(optimizer, last_epoch)
    
    def get_lr(self):
        return [ max( base_lr * ( 1 - self.last_epoch/self.max_iters )**self.power, self.min_lr)
                for base_lr in self.base_lrs]


class LRScheduler:
    def __init__(self, name, lr, iters_per_epoch, total_epochs, **kwargs):
        """
        Supported lr schedulers: [cos, warmcos, multistep]

        Args:
            lr (float): learning rate.
            iters_per_peoch (int): number of iterations in one epoch.
            total_epochs (int): number of epochs in training.
            kwargs (dict):
                - cos: None
                - warmcos: [warmup_epochs, warmup_lr_start (default 1e-6)]
                - multistep: [milestones (epochs), gamma (default 0.1)]
        """

        self.lr = lr
        self.iters_per_epoch = iters_per_epoch
        self.total_epochs = total_epochs
        self.total_iters = iters_per_epoch * total_epochs

        self.__dict__.update(kwargs)
        self.warmup_epochs = getattr(self, 'warmup_epochs', 0)

        self.lr_func = self._get_lr_func(name)

    def update_lr(self, iters):
        return self.lr_func(iters)

    def _get_lr_func(self, name):
        if name == "cos":  # cosine lr schedule
            lr_func = partial(cos_lr, self.lr, self.total_iters)
        elif name == "warmcos":
            warmup_total_iters = self.iters_per_epoch * self.warmup_epochs
            warmup_lr_start = getattr(self, "warmup_lr_start", 1e-6)
            lr_func = partial(
                warm_cos_lr,
                self.lr,
                self.total_iters,
                warmup_total_iters,
                warmup_lr_start,
            )
        elif name == "yoloxwarmcos":
            warmup_total_iters = self.iters_per_epoch * self.warmup_epochs
            no_aug_iters = self.iters_per_epoch * self.no_aug_epochs
            warmup_lr_start = getattr(self, "warmup_lr_start", 0)
            min_lr_ratio = getattr(self, "min_lr_ratio", 0.2)
            lr_func = partial(
                yolox_warm_cos_lr,
                self.lr,
                min_lr_ratio,
                self.total_iters,
                warmup_total_iters,
                warmup_lr_start,
                no_aug_iters,
            )
        elif name == "multistep":  # stepwise lr schedule
            milestones = [
                int(self.total_iters * milestone / self.total_epochs)
                for milestone in self.milestones
            ]
            gamma = getattr(self, "gamma", 0.1)
            lr_func = partial(multistep_lr, self.lr, milestones, gamma)
        elif name == "step":
            warmup_total_iters = self.iters_per_epoch * self.warmup_epochs
            gamma = getattr(self, "gamma", 0.1)
            lr_func = partial(step_lr, self.lr, gamma, warmup_total_iters)
        else:
            raise ValueError("Scheduler version {} not supported.".format(name))
        return lr_func


def cos_lr(lr, total_iters, iters):
    """Cosine learning rate"""
    lr *= 0.5 * (1.0 + math.cos(math.pi * iters / total_iters))
    return lr


def warm_cos_lr(lr, total_iters, warmup_total_iters, warmup_lr_start, iter):
    """Cosine learning rate with warm up."""
    if iter <= warmup_total_iters:
        lr = (lr - warmup_lr_start) * iter / float(warmup_total_iters) + warmup_lr_start
    else:
        lr *= 0.5 * (1.0 + math.cos(math.pi * (iter - warmup_total_iters)
                / (total_iters - warmup_total_iters)))
    return lr


def yolox_warm_cos_lr(
    lr,
    min_lr_ratio,
    total_iters,
    warmup_total_iters,
    warmup_lr_start,
    no_aug_iter,
    iter,
):
    """Cosine learning rate with warm up."""
    min_lr = lr * min_lr_ratio
    if iter <= warmup_total_iters:
        # lr = (lr - warmup_lr_start) * iters / float(warmup_total_iters) + warmup_lr_start
        lr = (lr - warmup_lr_start) * pow(iter / float(warmup_total_iters), 2) + warmup_lr_start
    elif iter >= total_iters - no_aug_iter:
        lr = min_lr
    else:
        lr = min_lr + 0.5 * (lr - min_lr) * (
            1.0
            + math.cos(
                math.pi
                * (iter - warmup_total_iters)
                / (total_iters - warmup_total_iters - no_aug_iter)
            )
        )
    return lr


def multistep_lr(lr, milestones, gamma, iter):
    """MultiStep learning rate"""
    for milestone in milestones:
        lr *= gamma if iter >= milestone else 1.0
    return lr


def step_lr(lr, gamma, total_iters, warmup_total_iters, iter):
    if iter <= warmup_total_iters:
        lr *= (gamma ** (iter / total_iters))
    else:
        lr *= (gamma ** ((iter - warmup_total_iters) / (total_iters - warmup_total_iters)))

    return lr
