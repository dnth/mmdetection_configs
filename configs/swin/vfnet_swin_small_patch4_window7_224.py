_base_ = [
    './vfnet_swin_tiny_patch4_window7_224.py'
]

model = dict(
    backbone=dict(
        depths=[2, 2, 18, 2]))

