{
    'variables': {
        'conditions': [
            ['OS=="mac"', {
                'clang_plugin_args': ''
            }],
        ]
    },
    'target_defaults': {
        'conditions': [
            ['OS=="win"', {
                'msvs_disabled_warnings': [4275, 4819, 4133, 4146, 4003]
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_C_LANGUAGE_STANDARD': 'gnu99',
                    'GCC_TREAT_WARNINGS_AS_ERRORS': 'NO'
                }
            }],
        ]
   }
}
