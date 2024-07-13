import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def add_1_vector(self,X):
        n,m = X.shape
        X_sum = np.sum(X,axis=0)
        if not isinstance(X_sum,np.ndarray):
            X_sum = X_sum.to_numpy()
        includes_1_vector = (X_sum[0] == n)
        if includes_1_vector:
            return m,X
        else:
            # Create a column vector of 1s with the same number of rows as X
            ones_column = np.ones((n, 1))

            # Horizontally stack the ones column with the input matrix X
            X = np.hstack((ones_column, X))
            return m+1, X



    def initialize_parameters(self, X):
        ## Checking if the X inputs contains a column of 1s
        m, X = self.add_1_vector(X)
        # _,m = X.shape
        self.weights = np.zeros(m)

    def compute_loss(self, y, y_hat):
        m = y.size if isinstance(y,np.ndarray) else y.shape[0]
        loss = -1/m * np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
        return loss

    def compute_gradients(self, X, y, y_hat):
        m, X = self.add_1_vector(X)
        # _,m = X.shape
        dw = 1/m * np.dot(X.T, (y_hat - y))
        return dw

    def fit(self, X, y):
        m, X = self.add_1_vector(X)
        self.initialize_parameters(X)
        
        for i in range(self.num_iterations):
            z = np.dot(X, self.weights)
            y_hat = self.sigmoid(z)
            loss = self.compute_loss(y, y_hat)
            
            dw = self.compute_gradients(X, y, y_hat)
            
            self.weights -= self.learning_rate * dw
            
            if i % 100 == 0:
                print(f'Loss after iteration {i:>4}: {loss:.4f}')

        print(f"Loss after FINAL iteration: {loss:.4f} (iterations={self.num_iterations:>6})")
        
    
    def predict(self, X,threshold=None):
        m, X = self.add_1_vector(X)
        z = np.dot(X, self.weights)
        y_hat = self.sigmoid(z)
        if threshold:
            y_pred = [1 if i > threshold else 0 for i in y_hat]
        else:
            y_pred = y_hat
        return np.array(y_pred)

# Example usage:
# X_train, y_train are the training data features and labels respectively
# X_train = np.array([[feature1, feature2], ...])
# y_train = np.array([label1, label2, ...])

# model = LogisticRegression(learning_rate=0.01, num_iterations=1000)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
