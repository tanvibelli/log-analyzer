from analyzer import count_failed 

def test_counts_failed_logins(): 
    counts = count_failed("sample.log")
    assert counts["203.0.113.5"] == 7

def tests_counts_other_ips(): 
    counts = count_failed("sample.log")
    assert counts["198.51.100.7"] == 2 
    assert counts["192.168.1.22"] == 1

def test_no_failures_gives_empty_counts(tmp_path): 
    log = tmp_path / "clean.log" 
    log.write_text("2026-11-12 08:01:12 SUCCESS 192.168.1.10 alice\n")
    assert count_failed(str(log)) == {}