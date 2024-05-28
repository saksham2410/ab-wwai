from ab_testing.models import User, db

class UserService:
    
    @staticmethod
    def create_user(hashed_id, attributes):
        new_user = User(hashed_id=hashed_id, attributes=attributes)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_hashed_id(hashed_id):
        return User.query.filter_by(hashed_id=hashed_id).first()
