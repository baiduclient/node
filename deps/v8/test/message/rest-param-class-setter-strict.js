// Copyright 2015 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// Flags: --harmony-rest-parameters
'use strict';

var _bad = "setting this should fail!";
class C {
  get bad() { return _bad; }
  set bad(...args) { _bad = args[0]; }
}
