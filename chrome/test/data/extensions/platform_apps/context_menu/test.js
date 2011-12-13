// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

function onclick(info) {
}

window.onload = function() {
  chrome.contextMenus.create({"title":"Extension Item 1",
                              "onclick": onclick}, function() {
    if (!chrome.extension.lastError) {
      chrome.test.sendMessage("created item");
    }
  });
};
