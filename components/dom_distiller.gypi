# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'conditions': [
    ['android_webview_build == 0', {
      'targets': [
        {
          'target_name': 'dom_distiller_webui',
          'type': 'static_library',
          'dependencies': [
            'component_resources.gyp:component_resources',
            'component_strings.gyp:component_strings',
            'distilled_page_proto',
            'dom_distiller_core',
            '../base/base.gyp:base',
            '../content/content.gyp:content_browser',
            '../skia/skia.gyp:skia',
            '../sync/sync.gyp:sync',
          ],
          'include_dirs': [
            '..',
          ],
          'sources': [
            'dom_distiller/webui/dom_distiller_handler.cc',
            'dom_distiller/webui/dom_distiller_handler.h',
            'dom_distiller/webui/dom_distiller_ui.cc',
            'dom_distiller/webui/dom_distiller_ui.h',
          ],
        },
        {
          'target_name': 'dom_distiller_core',
          'type': 'static_library',
          'dependencies': [
            'component_resources.gyp:component_resources',
            'distilled_page_proto',
            '../base/base.gyp:base',
            '../skia/skia.gyp:skia',
            '../sync/sync.gyp:sync',
            '../third_party/protobuf/protobuf.gyp:protobuf_lite',
            '../third_party/leveldatabase/leveldatabase.gyp:leveldatabase',
          ],
          'include_dirs': [
            '..',
          ],
          'export_dependent_settings': [
            'distilled_page_proto',
          ],
          'sources': [
            'dom_distiller/core/article_entry.cc',
            'dom_distiller/core/article_entry.h',
            'dom_distiller/core/distiller.cc',
            'dom_distiller/core/distiller.h',
            'dom_distiller/core/distiller_page.cc',
            'dom_distiller/core/distiller_page.h',
            'dom_distiller/core/distiller_url_fetcher.cc',
            'dom_distiller/core/distiller_url_fetcher.h',
            'dom_distiller/core/dom_distiller_constants.cc',
            'dom_distiller/core/dom_distiller_constants.h',
            'dom_distiller/core/dom_distiller_database.cc',
            'dom_distiller/core/dom_distiller_database.h',
            'dom_distiller/core/dom_distiller_model.cc',
            'dom_distiller/core/dom_distiller_model.h',
            'dom_distiller/core/dom_distiller_observer.h',
            'dom_distiller/core/dom_distiller_service.cc',
            'dom_distiller/core/dom_distiller_service.h',
            'dom_distiller/core/dom_distiller_store.cc',
            'dom_distiller/core/dom_distiller_store.h',
            'dom_distiller/core/page_distiller.cc',
            'dom_distiller/core/page_distiller.h',
            'dom_distiller/core/task_tracker.cc',
            'dom_distiller/core/task_tracker.h',
          ],
        },
        {
          'target_name': 'dom_distiller_test_support',
          'type': 'static_library',
          'dependencies': [
            'dom_distiller_core',
            '../sync/sync.gyp:sync',
            '../testing/gmock.gyp:gmock',
          ],
          'include_dirs': [
            '..',
          ],
          'sources': [
            'dom_distiller/core/dom_distiller_test_util.cc',
            'dom_distiller/core/dom_distiller_test_util.h',
            'dom_distiller/core/fake_db.cc',
            'dom_distiller/core/fake_db.h',
            'dom_distiller/core/fake_distiller.cc',
            'dom_distiller/core/fake_distiller.h',
          ],
        },
        {
          'target_name': 'distilled_page_proto',
          'type': 'static_library',
          'sources': [
            'dom_distiller/core/proto/distilled_article.proto',
            'dom_distiller/core/proto/distilled_page.proto',
          ],
          'variables': {
            'proto_in_dir': 'dom_distiller/core/proto',
            'proto_out_dir': 'components/dom_distiller/core/proto',
          },
          'includes': [ '../build/protoc.gypi' ]
        },
      ],
      'conditions': [
        ['OS != "ios"', {
          'targets': [
            {
              'target_name': 'dom_distiller_content',
              'type': 'static_library',
              'dependencies': [
                'component_resources.gyp:component_resources',
                'component_strings.gyp:component_strings',
                'dom_distiller_core',
                '../net/net.gyp:net',
                '../skia/skia.gyp:skia',
                '../sync/sync.gyp:sync',
              ],
              'include_dirs': [
                '..',
              ],
              'sources': [
                'dom_distiller/content/distiller_page_web_contents.cc',
                'dom_distiller/content/distiller_page_web_contents.h',
                'dom_distiller/content/dom_distiller_viewer_source.cc',
                'dom_distiller/content/dom_distiller_viewer_source.h',
              ],
            },
          ],
        }],
      ],
    }],
  ],
}
