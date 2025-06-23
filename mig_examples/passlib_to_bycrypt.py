from passlib.hash import bcrypt



    def password_valid(self, given_password):
        return bcrypt.verify(given_password, self.password)


    def set_password(self, new_password):
        self.password = bcrypt.encrypt(new_password)
