import numpy as np
from functools import lru_cache
import messages as msg
import math


class Vector:
    def __init__(self, v) -> None:
        """ Create a vector, example: v = Vector([1, 2, 3]) """
        try:
            if isinstance(v, np.ndarray):
                self.v = np.array(v)
            elif isinstance(v, list) or isinstance(v, tuple):
                self.v = np.array(v)
            else:
                raise Exception(msg.VECTOR_SHOULD_BE_LIST)
        except Exception as e:
            raise Exception(e)

    @lru_cache(1)
    def __len__(self) -> int:
        """ Get length of vector """
        return len(self.v)

    def __str__(self) -> str:
        """ String representation of the vector """
        return f"[{', '.join([str(i) for i in self.v])}]"

    def __repr__(self) -> str:
        """ String representation of the vector """
        return f"[{', '.join([str(i) for i in self.v])}]"

    def __getitem__(self, index) -> int:
        """ Get the value at a specific index """
        return self.v[index]

    def __setitem__(self, index, value) -> None:
        """ Set the value at a specific index """
        self.v[index] = value

    def __eq__(self, other) -> bool:
        """ Check if two vectors are equal """
        if isinstance(other, Vector):
            return np.array_equal(self.v, other.v)
        return False

    def __hash__(self) -> int:
        """ Generate a hash value for the vector """
        return hash(tuple(self.v))

    def __add__(self, other):
        """ Vector addition """
        if isinstance(other, Vector):
            return Vector(self.v + other.v)
        raise Exception("Unsupported operand type for +")

    def __sub__(self, other):
        """ Vector subtraction """
        if isinstance(other, Vector):
            return Vector(self.v - other.v)
        raise Exception("Unsupported operand type for -")

    def __mul__(self, scalar):
        """ Scalar multiplication """
        return Vector(self.v * scalar)

    def __rmul__(self, scalar):
        """ Scalar multiplication (reversed order) """
        return Vector(self.v * scalar)

    def dot(self, left, right) -> int:
        if len(left) != len(right):
            raise ValueError(
                "Vectors must have the same length for dot product")
        dot_product = sum(x * y for x, y in zip(left, right))
        return dot_product

    def cross(self, other):
        """ Cross product of two vectors (for 3D vectors) """
        if len(self.v) == 3 and len(other.v) == 3:
            cross_product = [
                self.v[1] * other.v[2] - self.v[2] * other.v[1],
                self.v[2] * other.v[0] - self.v[0] * other.v[2],
                self.v[0] * other.v[1] - self.v[1] * other.v[0]
            ]
            return Vector(cross_product)
        raise Exception("Cross product is defined for 3D vectors only")

    def magnitude(self) -> float:
        """ Magnitude (length) of the vector """
        return math.sqrt(sum(x**2 for x in self.v))

    def distance(self, other) -> float:
        """ Euclidean distance between two vectors """
        if isinstance(other, Vector):
            return math.sqrt(sum(x**2 for x in (self.v - other.v)))
        raise Exception("Unsupported operand type for distance")

    def validate_input_list(self, v) -> np.ndarray:
        """ Validating and getting numpy array from different types of input """
        if isinstance(v, np.ndarray):
            return v
        elif isinstance(v, list) or isinstance(v, tuple):
            return np.array(v)
        else:
            raise Exception(msg.VECTOR_SHOULD_BE_LIST)

    def validate_list(self, v=None) -> np.ndarray:
        """ Validating and getting numpy array from different types of input, if there is no input, return self vector """
        if isinstance(v, np.ndarray):
            return v
        elif isinstance(v, list) or isinstance(v, tuple):
            return np.array(v)
        elif self.v.size:
            return self.v
        else:
            raise Exception(msg.VECTOR_SHOULD_BE_LIST)

    def prepare_float_list(self, vlist) -> list[list[float]]:
        """ Building 2D array of arrays with float values """
        return [[float(i) for i in v] for v in vlist]

    def prepare_int_list(self, vlist) -> list[list[int]]:
        """ Building 2D array of arrays with int values """
        return [[int(i) for i in v] for v in vlist]

    def prepare_str_list(self, vlist) -> list[list[str]]:
        """ Building 2D array of arrays with str values """
        return [[str(i) for i in v] for v in vlist]

    def normalize(self, v=None) -> any:
        """ Vector normalization method """
        normalized = math.sqrt(sum(x**2 for x in v))
        return np.array(v).tolist() if normalized == 0 else np.array([x / normalized for x in v]).tolist()

    def lagrange(self, v1=None, v2=None, i_point=0) -> float:
        """ Method to find Lagrange Interpolation """
        if any(str(i).isdigit() for i in v1) == False or any(str(i).isdigit() for i in v2) == False:
            raise Exception(msg.NOT_ENOUGH_INPUT)
        if len(v1) != len(v2):
            raise Exception(msg.INPUT_SHOULD_SAME_SIZE)
        yp = 0
        for i in range(len(v1)):
            p = 1
            for j in range(len(v1)):
                if i != j:
                    p = p * (i_point - v1[j])/(v1[i] - v1[j])
            yp = yp + p * v2[i]
        return yp

    def l_dependence(self, vlist) -> bool:
        """ Method to find linear dependence """
        if isinstance(vlist, list):
            if any(isinstance(l, list) for l in vlist):
                vlist = [[float(i) for i in v] for v in vlist]
            else:
                raise Exception(msg.NO_LIST_OF_VECTOR)
        else:
            raise Exception(msg.NO_LIST_OF_VECTOR)
        return 'Linearly dependent' if np.linalg.matrix_rank(np.vstack(vlist).astype(float)) < len(vlist) else 'Linearly independent'

    def l_combination(self, vlist, coeffs) -> any:
        """ Method to find Linear Combination """
        result = self.dot(np.array(coeffs).T, np.array(vlist))
        return result.tolist() if isinstance(result, np.ndarray) else result

    def l_regression(self, v1=None, v2=None) -> str:
        """ Linear Regression Method using Least Square Method to find curve of best fit of type y=a+bx """
        if any(str(i).isdigit() for i in v1) == False or any(str(i).isdigit() for i in v2) == False:
            raise Exception(msg.NOT_ENOUGH_INPUT)
        if len(v1) != len(v2):
            raise Exception(msg.INPUT_SHOULD_SAME_SIZE)
        sumX, sumX2, sumY, sumXY = 0, 0, 0, 0
        for i in range(len(v1)):
            sumX = sumX + v1[i]
            sumX2 = sumX2 + v1[i]*v1[i]
            sumY = sumY + v2[i]
            sumXY = sumXY + v1[i]*v2[i]
        b = (len(v1)*sumXY-sumX*sumY)/(len(v1)*sumX2-sumX*sumX)
        a = (sumY - b*sumX)/len(v1)
        return f'y = {a} + {b}x'

    def gs(self, vlist=None) -> any:
        """ Gram-Schmidt method """
        if isinstance(vlist, list):
            if any(isinstance(l, list) for l in vlist):
                vlist = [[float(i) for i in v] for v in vlist]
            else:
                raise Exception(msg.EMPTY_LIST_OF_VECTOR)
        else:
            raise Exception(msg.NO_LIST_OF_VECTOR)
        orthogonal = []
        for v in vlist:
            v = np.array(v)
            for u in orthogonal:
                projection = self.dot(v, u) / self.dot(u, u)
                v -= projection * u
            if math.sqrt(sum(x**2 for x in self.v)) > 0:
                orthogonal.append(v)
        normalized_orthogonal = [self.normalize(v) for v in orthogonal]
        return np.array(normalized_orthogonal).tolist()
