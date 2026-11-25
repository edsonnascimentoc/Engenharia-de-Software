"""Compatibility entry point for the ALM auditor."""

from runpy import run_module


if __name__ == "__main__":
    run_module("src.alm_rtm_auditor", run_name="__main__")
