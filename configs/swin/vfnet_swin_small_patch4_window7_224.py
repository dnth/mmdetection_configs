_base_ = ["./vfnet_swin_tiny_patch4_window7_224.py"]

pretrained = 'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth'  # noqa

model = dict(
    backbone=dict(
        embed_dims=128,
        depths=[2, 2, 18, 2],
        num_heads=[4, 8, 16, 32],
        out_indices=(0, 1, 2, 3),
        init_cfg=dict(type='Pretrained', checkpoint=pretrained),
    ),
    neck=dict(
        in_channels=[128, 256, 512, 1024],
    ),
)
