#!/usr/bin/env python3

# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='nav2_map_server',
            node_executable='map_server',
            output='screen',
            arguments = [os.path.join(os.getenv('TEST_DIR'), 'testmap.yaml')])
            #arguments = [os.path.join(os.getenv('HOME'), 'ros2_overlay_ws/src/navigation2/src/mapping/nav2_map_server/test/testmap.yaml')])
])