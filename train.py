from demand_iq.pipelines.training_pipeline import TrainingPipeline

if __name__ == "__main__":

    pipeline = TrainingPipeline()

    model, metrics = pipeline.run_pipeline()

    print(metrics)