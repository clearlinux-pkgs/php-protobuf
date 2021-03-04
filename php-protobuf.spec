#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-protobuf
Version  : 3.15.4
Release  : 25
URL      : https://pecl.php.net/get/protobuf-3.15.4.tgz
Source0  : https://pecl.php.net/get/protobuf-3.15.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-protobuf-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev

%description
No detailed description available

%package lib
Summary: lib components for the php-protobuf package.
Group: Libraries

%description lib
lib components for the php-protobuf package.


%prep
%setup -q -n protobuf-3.15.4
cd %{_builddir}/protobuf-3.15.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/protobuf.so
