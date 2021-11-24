/*
  * Licensed to the Apache Software Foundation (ASF) under one or more
  * contributor license agreements. See the NOTICE file distributed with
  * this work for additional information regarding copyright ownership.
  * The ASF licenses this file to You under the Apache License, Version 2.0
  * (the "License"); you may not use this file except in compliance with
  * the License. You may obtain a copy of the License at

  * http://www.apache.org/licenses/LICENSE-2.0

  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
*/

import PropTypes from 'prop-types';
import React from 'react';
import { stringToSlug } from '../../utils/StringsUtils';

const StatusText = ({ text }) => {
  const classes =
    stringToSlug(text, '-') === 'ready-to-use' ? 'success' : 'danger';

  return (
    <>
      <i
        className={'fas fa-circle text-' + classes + ' mr-1'}
        data-testid="status-icon"
      />
      <span className={'text-' + classes} data-testid="status-text">
        {text}
      </span>
    </>
  );
};

StatusText.propTypes = {
  text: PropTypes.string.isRequired,
};

export default StatusText;