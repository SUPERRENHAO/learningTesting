import pytest

# 重写这个方法，自动添加标签等操作
def pytest_collection_modifyitems(session, config, items:list):
    # print(session)
    # print(config)
    # 自动添加标签
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
    # 倒叙
    # items.reverse()
# def err_to_fenmu(a,b):
#     print(a,b)
#     if b == 0 :
#         raise NameError("分母不能为0")
#     pass
# def err_to_string(a,b):
#     if isinstance(a,str) | isinstance(b,str) :
#         raise NameError("不能含有字符型")
#         pass
# def err_to_null(a,b):
#     if not a|b is None:
#         pass
#     else:
#         raise NameError("不能为空")

''' # pytest.ini文件的参数
  markers (linelist):   markers for test functions
  empty_parameter_set_mark (string):
                        default marker for empty parametersets
  norecursedirs (args): directory patterns to avoid for recursion
  testpaths (args):     directories to search for tests when no files or
                        directories are given in the command line.
  filterwarnings (linelist):
                        Each line specifies a pattern for
                        warnings.filterwarnings. Processed after
                        -W/--pythonwarnings.
  usefixtures (args):   list of default fixtures to be used with this project
  修改pytest可识别的为用例的文件开头
  python_files (args):  glob-style file patterns for Python test module
                        discovery
  修改pytest可识别的为用例的类
  python_classes (args):
                        prefixes or glob names for Python test class discovery
  修改pytest可识别为用例的方法
  python_functions (args):
                        prefixes or glob names for Python test function and
                        method discovery
  disable_test_id_escaping_and_forfeit_all_rights_to_community_support (bool):
                        disable string escape non-ascii characters, might cause
                        unwanted side effects(use at your own risk)
  console_output_style (string):
                        console output: "classic", or with additional progress
                        information ("progress" (percentage) | "count").
  xfail_strict (bool):  default for the strict parameter of xfail markers when
                        not given explicitly (default: False)
  enable_assertion_pass_hook (bool):
                        Enables the pytest_assertion_pass hook.Make sure to
                        delete any previously generated pyc cache files.
  junit_suite_name (string):
                        Test suite name for JUnit report
  junit_logging (string):
                        Write captured log messages to JUnit report: one of
                        no|log|system-out|system-err|out-err|all
  junit_log_passing_tests (bool):
                        Capture log information for passing tests to JUnit
                        report:
  junit_duration_report (string):
                        Duration time to report: one of total|call
  junit_family (string):
                        Emit XML for schema: one of legacy|xunit1|xunit2
  doctest_optionflags (args):
                        option flags for doctests
  doctest_encoding (string):
                        encoding used for doctest files
  cache_dir (string):   cache directory path.
  log_level (string):   default value for --log-level
  log_format (string):  default value for --log-format
  log_date_format (string):
                        default value for --log-date-format
  log_cli (bool):       enable log display during test run (also known as "live
                        logging").
  log_cli_level (string):
                        default value for --log-cli-level
  log_cli_format (string):
                        default value for --log-cli-format
  log_cli_date_format (string):
                        default value for --log-cli-date-format
  log_file (string):    default value for --log-file
  log_file_level (string):
                        default value for --log-file-level
  log_file_format (string):
                        default value for --log-file-format
  log_file_date_format (string):
                        default value for --log-file-date-format
  log_auto_indent (string):
                        default value for --log-auto-indent
  faulthandler_timeout (string):
                        Dump the traceback of all threads if a test takes more
                        than TIMEOUT seconds to finish.
  addopts (args):       extra command line options
  minversion (string):  minimally required pytest version
  required_plugins (args):
                        plugins that must be present for pytest to run
  render_collapsed (bool):
                        Open the report with all rows collapsed. Useful for very
                        large reports
  max_asset_filename_length (string):
                        set the maximum filename length for assets attached to
                        the html report.
  rsyncdirs (pathlist): list of (relative) paths to be rsynced for remote
                        distributed testing.
  rsyncignore (pathlist):
                        list of (relative) glob-style paths to be ignored for
                        rsyncing.
  looponfailroots (pathlist):
                        directories to check for changes
'''