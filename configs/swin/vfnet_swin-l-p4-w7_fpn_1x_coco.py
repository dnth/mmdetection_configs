_base_ = ["./vfnet_swin-t-p4-w7_fpn_1x_coco.py"]

pretrained = 'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_large_patch4_window7_224_22k.pth'  # noqa

model = dict(
    backbone=dict(
        embed_dims=192,
        depths=[2, 2, 18, 2],
        num_heads=[6, 12, 24, 48],
        out_indices=(0, 1, 2, 3),
        init_cfg=dict(type='Pretrained', checkpoint=pretrained),
    ),
    neck=dict(
        in_channels=[192, 256, 512, 1024],
    ),
)
