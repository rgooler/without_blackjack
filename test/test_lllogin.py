#!virtualenv/bin/python
# vim:fileencoding=utf8
import pytest
import withoutbj.lllogin

lll = withoutbj.lllogin.LLLogin()

def test_init():
	assert lll