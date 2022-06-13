from flask_restful import reqparse, Resource
import werkzeug
import cv2
import numpy as np
import src.services.calculate as calculate

parser = reqparse.RequestParser()
parser.add_argument('file',
                    type=werkzeug.datastructures.FileStorage,
                    location='files',
                    required=True,
                    help='provide a file')

class Calculator(Resource):
    def post(self):
        args = parser.parse_args()
        stream = args['file'].read()
        npimg = np.fromstring(stream, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        img = np.invert(np.array([img]))
        # cv2.imwrite("saved_file.jpg", img)
        result = calculate(img)
        response = { result }
        return response