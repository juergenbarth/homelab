docker network create \
--driver=bridge \
--ipv6 \
--subnet=172.20.0.0/24 \
--subnet=2001:db8::/112 \
proxy
