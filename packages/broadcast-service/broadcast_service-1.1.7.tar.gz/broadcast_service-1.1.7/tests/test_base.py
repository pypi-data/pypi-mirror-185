# Copyright 2022 Zeeland(https://github.com/Undertone0809/). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from unittest import TestCase
from broadcast_service import broadcast_service


def wait(seconds=0.5):
    time.sleep(seconds)


class TestBroadcast(TestCase):
    def test_listen_of_common(self):
        self.test_listen_of_common_no_params = False
        self.test_listen_of_common_specify_params = False

        def handle_topic_no_params():
            self.test_listen_of_common_no_params = True

        def handle_topic_specify_params(a, b, c):
            self.assertEqual(11, a)
            self.assertEqual(22, b)
            self.assertEqual(33, c)
            self.test_listen_of_common_specify_params = True

        broadcast_service.subscribe(
            "test_listen_of_common_no_params", handle_topic_no_params)
        broadcast_service.publish("test_listen_of_common_no_params")
        wait()
        self.assertTrue(self.test_listen_of_common_no_params)

        broadcast_service.subscribe(
            "test_listen_of_common_specify_params", handle_topic_specify_params)
        broadcast_service.publish(
            "test_listen_of_common_specify_params", 11, 22, 33)
        wait()
        self.assertTrue(self.test_listen_of_common_specify_params)

    def test_listen_of_decorator(self):
        self.test_listen_of_decorator_no_params = False
        self.test_listen_of_decorator_specify_params = False
        self.test_listen_of_decorator_listen_all = False
        self.counter = 0

        @broadcast_service.on_listen(["test_listen_of_decorator_no_params"])
        def handle_topic_no_params():
            self.test_listen_of_decorator_no_params = True

        @broadcast_service.on_listen(["test_listen_of_decorator_specify_params"])
        def handle_topic_specify_params(a, b, c):
            self.assertEqual(11, a)
            self.assertEqual(22, b)
            self.assertEqual(33, c)
            self.test_listen_of_decorator_specify_params = True

        @broadcast_service.on_listen()
        def handle_listen_all_topics(*args, **kwargs):
            self.counter += 1
            self.test_listen_of_decorator_listen_all = True

        broadcast_service.publish("test_listen_of_decorator_no_params")
        wait()
        self.assertTrue(self.test_listen_of_decorator_no_params)

        broadcast_service.publish(
            "test_listen_of_decorator_specify_params", 11, 22, 33)
        wait()
        self.assertTrue(self.test_listen_of_decorator_specify_params)

        broadcast_service.publish("test_listen_of_decorator_listen_all")
        wait()
        self.assertTrue(self.test_listen_of_decorator_listen_all)
        print(broadcast_service.pubsub_channels)
        self.assertEqual(3, self.counter)

    def test_listen_of_lambda(self):
        self.test_listen_of_lambda_no_params = False
        self.test_listen_of_lambda_specify_params = False

        def handle_topic_no_params():
            self.test_listen_of_lambda_no_params = True

        def handle_topic_specify_params(params: bool):
            self.test_listen_of_lambda_specify_params = params

        broadcast_service.subscribe(
            "test_listen_of_lambda_no_params", lambda: handle_topic_no_params())
        broadcast_service.publish("test_listen_of_lambda_no_params")
        wait()
        self.assertTrue(self.test_listen_of_lambda_no_params)

        broadcast_service.subscribe(
            "test_listen_of_lambda_specify_params", lambda: handle_topic_specify_params(True))
        broadcast_service.publish("test_listen_of_lambda_specify_params")
        wait()
        self.assertTrue(self.test_listen_of_lambda_no_params)

    def test_broadcast(self):
        pass

    def test_close(self):
        pass
