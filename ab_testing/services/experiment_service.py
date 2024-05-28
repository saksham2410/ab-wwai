from ab_testing.models import Experiment, db

class ExperimentService:

    @staticmethod
    def create_experiment(name, description, start_date, end_date, status):
        new_experiment = Experiment(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status=status
        )
        db.session.add(new_experiment)
        db.session.commit()
        return new_experiment

    @staticmethod
    def get_all_experiments():
        return Experiment.query.all()
