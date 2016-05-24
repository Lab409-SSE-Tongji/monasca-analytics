#!/usr/bin/env python

# Copyright (c) 2016 Hewlett Packard Enterprise Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not used this file except in compliance with the License. You may obtain
# a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import numpy as np

from main.sml import svm_one_class as svm


class MockClassifier():

    def __init__(self, predict_anomaly=False):
        self._predict_anomaly = predict_anomaly
        self.predict_cnt = 0

    def predict(self, _):
        self.predict_cnt += 1
        if self._predict_anomaly:
            return np.array([svm.ANOMALY])
        return np.array([svm.NON_ANOMALY])
