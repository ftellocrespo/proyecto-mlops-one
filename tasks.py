from invoke import task

@task
def ingest(ctx):
    ctx.run("python src/data_eng/stage1_ingestion.py")

@task
def clean(ctx):
    ctx.run("python src/data_eng/stage2_cleaning.py")

@task
def features(ctx):
    ctx.run("python src/data_eng/stage3_labeling.py")

@task
def split(ctx):
    ctx.run("python src/data_eng/stage4_splitting.py")

@task
def data_eng_pipeline(ctx):
    ingest(ctx)
    clean(ctx)
    features(ctx)
    split(ctx)