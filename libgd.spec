#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgd
Version  : 2.2.5
Release  : 32
URL      : https://github.com/libgd/libgd/releases/download/gd-2.2.5/libgd-2.2.5.tar.xz
Source0  : https://github.com/libgd/libgd/releases/download/gd-2.2.5/libgd-2.2.5.tar.xz
Summary  : GD graphics library
Group    : Development/Tools
License  : MIT
Requires: libgd-bin = %{version}-%{release}
Requires: libgd-lib = %{version}-%{release}
Requires: libgd-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(xpm)
BuildRequires : zlib-dev
Patch1: cve-2016-7568.patch
Patch2: CVE-2018-1000222.patch

%description
GD Graphics (Draw) Library. GD is an open source code library for the dynamic
creation of images by programmers. GD is written in C, and "wrappers" are
available for Perl, PHP and other languages. GD can read and write many
different image formats. GD is commonly used to generate charts, graphics,
thumbnails, and most anything else, on the fly.

%package bin
Summary: bin components for the libgd package.
Group: Binaries
Requires: libgd-license = %{version}-%{release}

%description bin
bin components for the libgd package.


%package dev
Summary: dev components for the libgd package.
Group: Development
Requires: libgd-lib = %{version}-%{release}
Requires: libgd-bin = %{version}-%{release}
Provides: libgd-devel = %{version}-%{release}

%description dev
dev components for the libgd package.


%package lib
Summary: lib components for the libgd package.
Group: Libraries
Requires: libgd-license = %{version}-%{release}

%description lib
lib components for the libgd package.


%package license
Summary: license components for the libgd package.
Group: Default

%description license
license components for the libgd package.


%prep
%setup -q -n libgd-2.2.5
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539716220
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1539716220
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgd
cp src/COPYING %{buildroot}/usr/share/package-licenses/libgd/src_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/annotate
/usr/bin/bdftogd
/usr/bin/gd2copypal
/usr/bin/gd2togif
/usr/bin/gd2topng
/usr/bin/gdcmpgif
/usr/bin/gdlib-config
/usr/bin/gdparttopng
/usr/bin/gdtopng
/usr/bin/giftogd2
/usr/bin/pngtogd
/usr/bin/pngtogd2
/usr/bin/webpng

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libgd.so
/usr/lib64/pkgconfig/gdlib.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgd.so.3
/usr/lib64/libgd.so.3.0.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgd/src_COPYING
