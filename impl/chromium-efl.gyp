{
  'variables': {
    'data_dir%': '/usr/share/chromium-efl/',
    'exe_dir%': '/usr/lib/chromium-efl/',
    'edje_dir%': '/usr/share/chromium-efl/themes/',
    'locale_dir%': '/usr/share/chromium-efl/locale/',
    'webdb_dir%': '/usr/share/chromium-efl/db/',
    'edje_compiler%': 'edje_cc',
    'chromium_efl_library_type%': 'shared_library',
  },
  'target_defaults': {
    'conditions': [
     ['custom_libc_dir!=""', {
       'ldflags': [
         # We want to statically link libstdc++/libgcc_s.
         '-static-libstdc++',
         '-static-libgcc',
         '-Wl,-rpath,<(custom_libc_dir)',
         '-Wl,--dynamic-linker=<(custom_libc_dir)/ld-linux.so.3',
       ],
     }],
    ],
    'defines': [
      'DATA_DIR="<(data_dir)"',
      'EXE_DIR="<(exe_dir)"',
      'EDJE_DIR="<(edje_dir)"',
      'WEBDB_DIR="<(webdb_dir)"',
    ],
  },
  'targets': [{
    'target_name': 'chromium-efl',
    'type': '<(chromium_efl_library_type)',
    'includes': [
      # NOTE: gyp includes need to be relative
      '../src/skia/skia_common.gypi',
    ],
    'include_dirs': [
      '.',
      '<(chrome_src_dir)',
      '<(chrome_src_dir)/third_party/WebKit', # [M34] without this, build errors occur due to #include path changes in M34. for example, see WebFrame.h.
      '<(chrome_src_dir)/third_party/skia/include/core',
      '<(chrome_src_dir)/third_party/mesa/src/include',
      '<(chrome_src_dir)/v8/include',

      '<(PRODUCT_DIR)/gen',
      '<(SHARED_INTERMEDIATE_DIR)',
      '<(SHARED_INTERMEDIATE_DIR)/ui/gl/',
      '<(SHARED_INTERMEDIATE_DIR)/webkit/',
    ],
    'dependencies': [
      'chromium-efl-deps.gyp:efl',
      'chromium-efl-deps.gyp:gstreamer',
      'theme/theme.gyp:tizen_theme',
      '<(chrome_src_dir)/base/allocator/allocator.gyp:allocator',
      '<(chrome_src_dir)/content/content.gyp:content',
      '<(chrome_src_dir)/content/content.gyp:content_app_browser',
      '<(chrome_src_dir)/content/content_shell_and_tests.gyp:content_shell_resources',
      '<(chrome_src_dir)/content/content_shell_and_tests.gyp:content_shell_pak',
      '<(chrome_src_dir)/components/components.gyp:visitedlink_browser',
      '<(chrome_src_dir)/components/components.gyp:visitedlink_renderer',
      '<(chrome_src_dir)/third_party/icu/icu.gyp:icuuc',
      '<(chrome_src_dir)/components/components.gyp:sessions_content',
# [M37] TODO:Autofill related code chagned. Need to enable after Fixing.
      #'<(chrome_src_dir)/components/components.gyp:autofill_content_renderer',
      #'<(chrome_src_dir)/components/components.gyp:autofill_content_browser',
      #'<(chrome_src_dir)/components/components.gyp:password_manager_core_common',
      #'<(chrome_src_dir)/components/components.gyp:password_manager_core_browser',
    ],
    'defines': [
      'CHROMIUMCORE_IMPLEMENTATION=1',
      'TIZEN_WEBVIEW_IMPLEMENTATION=1',
      'LOCALE_DIR="<(locale_dir)"',
    ],
    'sources': [
      # Extra cc files from chrome_src_dir
      '<(chrome_src_dir)/ui/events/gestures/gesture_recognizer_impl.h',
      '<(chrome_src_dir)/ui/events/gestures/gesture_recognizer_impl.cc',
      # We do not have gesture recognizer for EFL, try to reuse aura recognizer
      '<(chrome_src_dir)/ui/events/gestures/gesture_provider_aura.h',
      '<(chrome_src_dir)/ui/events/gestures/gesture_provider_aura.cc',
      '<(chrome_src_dir)/ui/events/gestures/motion_event_aura.h',
      '<(chrome_src_dir)/ui/events/gestures/motion_event_aura.cc',
      '<(chrome_src_dir)/ui/base/nine_image_painter_factory.h',
      '<(chrome_src_dir)/ui/base/nine_image_painter_factory.cc',
      '<(chrome_src_dir)/ui/base/cursor/cursor.h',
      '<(chrome_src_dir)/ui/base/cursor/cursor.cc',
      '<(chrome_src_dir)/ui/base/cursor/cursor_x11.cc',
      '<(chrome_src_dir)/ui/base/cursor/cursor_loader_x11.h',
      '<(chrome_src_dir)/ui/base/cursor/cursor_loader_x11.cc',
      '<(chrome_src_dir)/ui/base/cursor/cursors_aura.h',
      '<(chrome_src_dir)/ui/base/cursor/cursors_aura.cc',
      '<(chrome_src_dir)/ui/gfx/nine_image_painter.h',
      '<(chrome_src_dir)/ui/gfx/nine_image_painter.cc',

      # API
      'API/ewk_auth_challenge_private.h',
      'API/ewk_autofill_profile_private.h',
      'API/ewk_autofill_profile_private.cc',
      'API/ewk_certificate_private.h',
      'API/ewk_console_message_private.h',
      'API/ewk_context_menu_private.h',
      'API/ewk_cookie_manager_private.h',
      'API/ewk_error_private.h',
      'API/ewk_geolocation_private.cc',
      'API/ewk_geolocation_private.h',
      'API/ewk_hit_test_private.cc',
      'API/ewk_hit_test_private.h',
      'API/ewk_policy_decision_private.cc',
      'API/ewk_policy_decision_private.h',
      'API/ewk_security_origin_private.h',
      'API/ewk_settings_private.cc',
      'API/ewk_settings_private.h',
      'API/ewk_suspendable_object.cc',
      'API/ewk_suspendable_object.h',
      'API/ewk_text_style_private.h',
      'API/ewk_user_media_private.h',
      'API/ewk_web_application_icon_data_private.h',
      'API/ewk_web_application_icon_data_private.cc',
      'API/ewk_window_features_private.h',
      'EdgeEffect.cpp',
      'EdgeEffect.h',
      'browser/autofill/autofill_manager_delegate_efl.cc',
      'browser/autofill/autofill_manager_delegate_efl.h',
      'browser/autofill/personal_data_manager_factory.cc',
      'browser/autofill/personal_data_manager_factory.h',
      'browser/device_sensors/data_fetcher_impl_tizen.cc',
      'browser/device_sensors/data_fetcher_impl_tizen.h',
      'browser/device_sensors/data_fetcher_shared_memory_tizen.cc',
      'browser/disambiguation_popup_efl.cc',
      'browser/disambiguation_popup_efl.h',
      'browser/download_manager_delegate_efl.cc',
      'browser/download_manager_delegate_efl.h',
      'browser/favicon/favicon_commands.cc',
      'browser/favicon/favicon_commands.h',
      'browser/favicon/favicon_database.cc',
      'browser/favicon/favicon_database.h',
      'browser/favicon/favicon_database_p.cc',
      'browser/favicon/favicon_database_p.h',
      'browser/favicon/favicon_downloader.cc',
      'browser/favicon/favicon_downloader.h',
      'browser/favicon/favicon_service.cc',
      'browser/favicon/favicon_service.h',
      'browser/geolocation/access_token_store_efl.cc',
      'browser/geolocation/access_token_store_efl.h',
      'browser/geolocation/geolocation_permission_context_efl.cc',
      'browser/geolocation/geolocation_permission_context_efl.h',
      'browser/geolocation/location_provider_efl.cc',
      'browser/geolocation/location_provider_efl.h',
      'browser/inputpicker/InputPicker.cc',
      'browser/inputpicker/InputPicker.h',
      'browser/inputpicker/color_chooser_efl.cc',
      'browser/inputpicker/color_chooser_efl.h',
      'browser/javascript_dialog_manager_efl.cc',
      'browser/javascript_dialog_manager_efl.h',
      'browser/javascript_modal_dialog_efl.cc',
      'browser/javascript_modal_dialog_efl.h',
      'browser/login_delegate_efl.cc',
      'browser/login_delegate_efl.h',
      'browser/motion/wkext_motion.cc',
      'browser/motion/wkext_motion.h',
      'browser/motion/MotionUI.cc',
      'browser/motion/MotionUI.h',
      'browser/navigation_policy_handler_efl.cc',
      'browser/navigation_policy_handler_efl.h',
      'browser/password_manager/password_manager_client_efl.cc',
      'browser/password_manager/password_manager_client_efl.h',
      'browser/password_manager/content_password_manager_driver.cc',
      'browser/password_manager/content_password_manager_driver.h',
      'browser/password_manager/password_form_manager.cc',
      'browser/password_manager/password_form_manager.h',
      'browser/password_manager/password_generation_manager.cc',
      'browser/password_manager/password_generation_manager.h',
      'browser/password_manager/password_manager.cc',
      'browser/password_manager/password_manager.h',
      'browser/password_manager/password_manager_client.cc',
      'browser/password_manager/password_manager_client.h',
      'browser/password_manager/password_manager_driver.h',
      'browser/password_manager/password_manager_util.h',
      'browser/password_manager/password_manager_util_efl.cc',
      'browser/password_manager/password_store_factory.cc',
      'browser/password_manager/password_store_factory.h',
      'browser/policy_response_delegate_efl.cc',
      'browser/policy_response_delegate_efl.h',
      'browser/renderer_host/browsing_data_remover_efl.cc',
      'browser/renderer_host/browsing_data_remover_efl.h',
      'browser/renderer_host/im_context_efl.cc',
      'browser/renderer_host/im_context_efl.h',
      'browser/renderer_host/native_web_keyboard_event_efl.cc',
      'browser/renderer_host/render_message_filter_efl.cc',
      'browser/renderer_host/render_message_filter_efl.h',
      'browser/renderer_host/render_widget_host_view_efl.cc',
      'browser/renderer_host/render_widget_host_view_efl.h',
      'browser/renderer_host/scroll_detector.cc',
      'browser/renderer_host/scroll_detector.h',
      # The same files is present in src/content, do we need another copy if it?
      #'browser/renderer_host/touchpad_tap_suppression_controller_efl.cc',
      'browser/renderer_host/web_cache_manager_efl.cc',
      'browser/renderer_host/web_cache_manager_efl.h',
      'browser/renderer_host/web_event_factory_efl.cc',
      'browser/renderer_host/web_event_factory_efl.h',
      'browser/resource_dispatcher_host_delegate_efl.h',
      'browser/resource_dispatcher_host_delegate_efl.cc',
      'browser/resource_throttle_efl.cc',
      'browser/resource_throttle_efl.h',
      'browser/scoped_wait_for_ewk.h',
      'browser/selectpicker/WebPopupItem.cc',
      'browser/selectpicker/WebPopupItem.h',
      'browser/selectpicker/popup_menu_item.cc',
      'browser/selectpicker/popup_menu_item.h',
      'browser/selectpicker/popup_menu_item_private.h',
      'browser/selectpicker/popup_picker.cc',
      'browser/selectpicker/popup_picker.h',
      'browser/sound_effect.h',
      'browser/sound_effect.cc',
      'browser/sound_effect_tizen.cc',
      'browser/vibration/vibration_message_filter.cc',
      'browser/vibration/vibration_message_filter.h',
      'browser/vibration/vibration_provider_client.cc',
      'browser/vibration/vibration_provider_client.h',
      'browser/web_contents/web_contents_view_efl.cc',
      'browser/web_contents/web_contents_view_efl.h',
      'browser/web_contents/web_drag_dest_efl.cc',
      'browser/web_contents/web_drag_dest_efl.h',
      'browser/web_view_browser_message_filter.h',
      'browser/web_view_browser_message_filter.cc',
      'browser/webdata/web_data_service.cc',
      'browser/webdata/web_data_service.h',
      'browser/webdata/web_data_service_factory.h',
      'browser/webdata/web_data_service_factory.cc',
      'browser_context_efl.cc',
      'browser_context_efl.h',
      'browser_main_parts_efl.cc',
      'browser_main_parts_efl.h',
      'cache_params_efl.h',
      'command_line_efl.cc',
      'command_line_efl.h',

      'common/content_client_efl.cc',
      'common/content_client_efl.h',
      'common/content_switches_efl.cc',
      'common/content_switches_efl.h',
      'common/message_generator_efl.cc',
      'common/message_generator_efl.h',
      'common/render_messages_efl.h',
      'common/version_info.cc',
      'common/version_info.h',
      'common/version_info_efl.h',
      'common/web_contents_utils.cc',
      'common/web_contents_utils.h',
      'common/cursors/webcursor_efl.cc',
      'common/cursors/webcursor_efl.h',
      'components/clipboard/clipboard_efl.cc',
      'components/clipboard/clipboard_efl.h',
      'components/clipboard/clipboard_helper_efl.cc',
      'components/clipboard/clipboard_helper_efl.h',
      'components/editing/content/browser/editor_client_observer.cc',
      'components/editing/content/browser/editor_client_observer.h',
      'components/editing/content/common/editing_messages.h',
      'components/editing/content/renderer/editorclient_agent.cc',
      'components/editing/content/renderer/editorclient_agent.h',
      'content_browser_client_efl.cc',
      'content_browser_client_efl.h',
      'autofill_popup_view_efl.h',
      'autofill_popup_view_efl.cc',
      'content_main_delegate_efl.cc',
      'content_main_delegate_efl.h',
      'context_menu_controller_efl.cc',
      'context_menu_controller_efl.h',
      'cookie_manager.cc',
      'cookie_manager.h',
      'device/battery/battery_status_manager_tizen.cc',
      'device/battery/battery_status_manager_tizen.h',
      'devtools_delegate_efl.cc',
      'devtools_delegate_efl.h',
      'devtools_manager_delegate_efl.cc',
      'devtools_manager_delegate_efl.h',
      'eweb_context.cc',
      'eweb_context.h',
      'eweb_view.cc',
      'eweb_view.h',
      'eweb_view_callbacks.h',
      'ewk_global_data.h',
      'ewk_global_data.cc',
      'file_chooser_controller_efl.cc',
      'file_chooser_controller_efl.h',
      'gfx/x11_event_source_efl.cc',
      'gfx/x11_types_override.cc',
      'gl/gl_context_egl_override.cc',
      'gl/gl_current_context_efl.cc',
      'gl/gl_shared_context_efl.cc',
      'gl/gl_shared_context_efl.h',
      'gpu/gpu_thread_override_efl.cc',
      'gpu/gpu_thread_override_efl.h',
      'http_user_agent_settings_efl.cc',
      'http_user_agent_settings_efl.h',
      'memory_purger.cc',
      'memory_purger.h',
      'message_pump_for_ui_efl.cc',
      'message_pump_for_ui_efl.h',
      'navigation_policy_params.h',
      'network_delegate_efl.cc',
      'network_delegate_efl.h',
      'paths_efl.cc',
      'paths_efl.h',
      'popup_controller_efl.cc',
      'popup_controller_efl.h',
      'renderer/content_renderer_client_efl.cc',
      'renderer/content_renderer_client_efl.h',
      'renderer/print_pages_params.cc',
      'renderer/print_pages_params.h',
      'renderer/print_web_view_helper_efl.cc',
      'renderer/print_web_view_helper_efl.h',
      'renderer/render_frame_observer_efl.cc',
      'renderer/render_frame_observer_efl.h',
      'renderer/render_process_observer_efl.cc',
      'renderer/render_process_observer_efl.h',
      'renderer/render_view_observer_efl.cc',
      'renderer/render_view_observer_efl.h',

      'resource/resource_bundle_efl.cc',

      'resource/JavaScriptPopup.edc',
      'resource/AutofillPopup.edc',
      'resource/Edge.edc',
      'resource/Magnifier.edc',
      'resource/control.edc',
      'resource/DisambiguationPopup.edc',

      'ui/native_theme/native_theme_efl.h',
      'ui/native_theme/native_theme_efl.cc',
      'ui/snapshot/snapshot_efl.cc',
      'ui/events/gesture_detection/gesture_configuration_efl.cc',

      'screen_efl.cc',
      'screen_efl.h',
      'selection_box_efl.cc',
      'selection_box_efl.h',
      'selection_controller_efl.cc',
      'selection_controller_efl.h',
      'selection_handle_efl.cc',
      'selection_handle_efl.h',
      'selection_magnifier_efl.cc',
      'selection_magnifier_efl.h',
      # tizen_webview
      #TODO: making separate gyp for tizen_webview
      'tizen_webview/public/tw_back_forward_history.h',
      'tizen_webview/public/tw_back_forward_history.cc',
      'tizen_webview/public/tw_back_forward_list.h',
      'tizen_webview/public/tw_back_forward_list_impl.h',
      'tizen_webview/public/tw_back_forward_list_impl.cc',
      'tizen_webview/public/tw_content_security_policy.h',
      'tizen_webview/public/tw_context_menu_controller.h',
      'tizen_webview/public/tw_context_menu_controller.cc',
      'tizen_webview/public/tw_custom_handlers.h',
      'tizen_webview/public/tw_custom_handlers.cc',
      'tizen_webview/public/tw_frame.h',
      'tizen_webview/public/tw_frame.cc',
      'tizen_webview/public/tw_hit_test.h',
      'tizen_webview/public/tw_hit_test.cc',
      'tizen_webview/public/tw_notification.cc',
      'tizen_webview/public/tw_notification.h',
      'tizen_webview/public/tw_policy_decision.h',
      'tizen_webview/public/tw_policy_decision.cc',
      'tizen_webview/public/tw_security_origin.cc',
      'tizen_webview/public/tw_security_origin.h',
      'tizen_webview/public/tw_selection_controller.h',
      'tizen_webview/public/tw_selection_controller.cc',
      'tizen_webview/public/tw_touch_point.h',
      'tizen_webview/public/tw_touch_point.cc',
      'tizen_webview/public/tw_url.cc',
      'tizen_webview/public/tw_url.h',
      'tizen_webview/public/tw_web_context.h',
      'tizen_webview/public/tw_web_context.cc',
      'tizen_webview/public/tw_webview.cc',
      'tizen_webview/public/tw_webview_delegate.h',
      'tizen_webview/public/tw_webview_delegate.cc',
      'tizen_webview/public/tw_webview_evas_event_handler.h',
      'tizen_webview/public/tw_webview_evas_event_handler.cc',
      'tizen_webview/public/tw_wrt.h',
      'tizen_webview/public/tw_wrt.h',
      'tizen_webview/public/tw_wrt.cc',
      'tizen_webview/tw_misc_utility.h',
      'tizen_webview/tw_misc_utility.cc',
      'url_request_context_getter_efl.cc',
      'url_request_context_getter_efl.h',
      'web_contents_delegate_efl.cc',
      'web_contents_delegate_efl.h',
      'web_process_content_main_delegate_efl.cc',
      'web_process_content_main_delegate_efl.h',
      'wrt/dynamicplugin.cc',
      'wrt/dynamicplugin.h',
      'wrt/wrtwidget.cc',
      'wrt/wrtwidget.h',

      # Temporary fix for M40 build
      'third_party/webrtc/system_wrappers/source/cpu_features_tizen.c',
    ],
    'cflags!': [
      # Symbol visibility controled by chromium-efl.filter
      '-fvisibility=hidden',
    ],
    'link_settings': {
      'ldflags': [
        '-Wl,--no-undefined',
        '-Wl,--version-script,<(efl_impl_dir)/chromium-efl.filter',
        '-rdynamic',
      ],
      'conditions': [
        ['_toolset=="target"', {
          'libraries': [ '<!($(echo ${CXX_target:-g++}) -print-libgcc-file-name)', ]
        }],
      ],
    },
    'rules': [{
        'rule_name': 'edje_resources',
        'message': 'Compiling edje files <(RULE_INPUT_NAME)',
        'extension': 'edc',
        'outputs': [
          '<(PRODUCT_DIR)/resources/<(RULE_INPUT_ROOT).edj',
        ],
        'action': [
          '<(edje_compiler)',
          '-id', 'resource/images',
          '<(RULE_INPUT_PATH)',
          '<(PRODUCT_DIR)/resources/<(RULE_INPUT_ROOT).edj',
        ],
    }], # rules
    'conditions': [
      ['tizen_multimedia_support==1', {
        'includes': [
          'chromium-efl-mm.gypi',
        ],
      }],
      ['building_for_tizen==1', {
        'sources': [
          'content/common/gpu/client/gpu_memory_buffer_impl_efl.cc',
          'content/common/gpu/client/gpu_memory_buffer_impl_efl_pixmap.cc',
          'content/common/gpu/client/gpu_memory_buffer_impl_efl_pixmap.h',
          'content/common/gpu/gpu_memory_buffer_factory_efl.cc',
          'content/common/gpu/gpu_memory_buffer_factory_efl_pixmap.cc',
          'content/common/gpu/gpu_memory_buffer_factory_efl_pixmap.h',
          'ui/gl/gl_image_efl_pixmap.cc',
          'ui/gl/gl_image_efl_pixmap.h',
          'ui/gl/efl_pixmap.cc',
          'ui/gl/efl_pixmap.h',
        ],
        'dependencies': [ 'chromium-efl-deps.gyp:tizen' ],
        'link_settings': {
          'libraries': [
            '-ldrm',
            '-lEGL',
            '-lGLESv2',
          ],
        },
      }],
      ['building_for_tizen_mobile==1', {
        'sources': [
          'browser/speech/tts_message_filter_efl.cc',
          'browser/speech/tts_message_filter_efl.h',
          'browser/speech/tts_tizen.cc',
          'browser/speech/tts_tizen.h',
          'common/tts_messages_efl.h',
          'common/tts_utterance_request_efl.cc',
          'common/tts_utterance_request_efl.h',
          'renderer/tts_dispatcher_efl.cc',
          'renderer/tts_dispatcher_efl.h',
        ],
      }],
      ['ewk_bringup==1', {
        'defines': [ 'EWK_BRINGUP=1' ],
        'defines!': [ 'TIZEN_CONTENTS_DETECTION=1' ],
      }],
      ['prebuilt_ld_gold_dir!=""', {
        'ldflags': [
          '-B<(prebuilt_ld_gold_dir)',
        ],
      } , { # prebuild_ld_gold_dir == ""
        'ldflags': [
          # Building the RPM in the GBS chroot fails with errors such as
          # [  XXs] error: create archive failed on file /<path>/libchromium-efl.so: cpio: Bad magic
          # [  XXs] RPM build errors:
          # [  XXs]     create archive failed on file /<path>/libchromium-efl.so: cpio: Bad magic
          # For now, work around it by passing a GNU ld-specific flag that optimizes the
          # linker for memory usage.
          # http://107.108.218.239/bugzilla/show_bug.cgi?id=6457
          '-Wl,--no-keep-memory',
        ],
      }],
      ['enable_basic_printing==0 and enable_print_preview==0', {
        'sources!': [
          'renderer/print_pages_params.cc',
          'renderer/print_pages_params.h',
          'renderer/print_web_view_helper_efl.cc',
          'renderer/print_web_view_helper_efl.h',
        ],
      }],
      ['notifications==1', {
        'sources': [
          'browser/notification/notification_controller_efl.cc',
          'browser/notification/notification_controller_efl.h',
        ],
      }],
    ],
  },
  {
    'target_name': 'efl_webprocess',
    'type': 'executable',
    'include_dirs': [
      '.',
    ],
    'sources': [
      'web_process.cc',
    ],
    'dependencies': [
      'chromium-efl',
    ],
  },
  {
    'target_name': 'content_shell_efl',
    'type': 'executable',
    'dependencies': [
      'chromium-efl-deps.gyp:efl',
      'theme/theme.gyp:tizen_theme',
      '<(chrome_src_dir)/content/content_shell_and_tests.gyp:content_shell_lib',
      '<(chrome_src_dir)/content/content_shell_and_tests.gyp:content_shell_pak',
      '<(chrome_src_dir)/breakpad/breakpad.gyp:minidump_stackwalk',
      '<(chrome_src_dir)/breakpad/breakpad.gyp:dump_syms',
      '<(chrome_src_dir)/tools/imagediff/image_diff.gyp:image_diff',
      '<(chrome_src_dir)/base/allocator/allocator.gyp:allocator',
      '<(chrome_src_dir)/sandbox/sandbox.gyp:sandbox',
      'chromium-efl',
    ],
    'sources': [
      'shell/shell_efl.cc',
      'shell/shell_main.cc',
      'shell/shell_web_contents_view_delegate_efl.cc',
      'shell/message_pump_efl.h',
      'shell/message_pump_efl.cc',
    ],
    'include_dirs': [
      '.',
    ],
    'conditions': [
      ['prebuilt_ld_gold_dir!=""', {
        'ldflags': [
          '-B<(prebuilt_ld_gold_dir)',
        ],
      } , { # prebuild_ld_gold_dir == ""
        'ldflags': [
          # Building the RPM in the GBS chroot fails with errors such as
          # [  XXs] error: create archive failed on file /<path>/libchromium-efl.so: cpio: Bad magic
          # [  XXs] RPM build errors:
          # [  XXs]     create archive failed on file /<path>/libchromium-efl.so: cpio: Bad magic
          # For now, work around it by passing a GNU ld-specific flag that optimizes the
          # linker for memory usage.
          # http://107.108.218.239/bugzilla/show_bug.cgi?id=6457
          '-Wl,--no-keep-memory',
        ],
      }],
    ],
  },
  ],
}
