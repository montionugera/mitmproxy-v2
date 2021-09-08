
#Run
### Run by Docker

# cd dev dir
`
docker run \
        -v $(pwd)/.mitmproxy:/home/mitmproxy/.mitmproxy \
        -v $(pwd)/scripts:/home/mitmproxy/scripts \
        --rm -it -p 8080:8080 -p 127.0.0.1:8081:8081 \
        mitmproxy/mitmproxy \
        mitmweb --web-host 0.0.0.0 --mode socks5 --showhost \
        -s /home/mitmproxy/scripts/example.py
`
docker run \
        -v $(pwd)/.mitmproxy:/home/mitmproxy/.mitmproxy \
        -v $(pwd)/scripts:/home/mitmproxy/scripts \
        --rm -it -p 8080:8080 -p 127.0.0.1:8082:8081 \
        mitmproxy/mitmproxy \
        mitmweb --web-host 0.0.0.0 --mode socks5 --showhost \
        -s /home/mitmproxy/scripts/example.py


mimt.it