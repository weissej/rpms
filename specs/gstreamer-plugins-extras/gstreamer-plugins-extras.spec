%define		gst_minver	0.8.4
%define		gstp_minver	0.8.5
%define		majorminor	0.8
%define		gstreamer	gstreamer
%define		register	%{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1 || :

%define		gstplugs	mpeg1sys mpeg1videoparse mpeg2sub mpegaudio mpegaudioparse mpegstream
%define		extplugs	a52dec dvdnav dvdread faad gsm lame libfame mad mpeg2dec musepack swfdec

Name:		%{gstreamer}-plugins-extra
Version:	0.8.6
Release:	1
Summary:	GStreamer extra streaming media framework plugins

Group:		Applications/Multimedia
License:	LGPL
URL:		http://gstreamer.net/
Source:		http://gstreamer.freedesktop.org/src/gst-plugins/gst-plugins-%{version}.tar.bz2
Patch:		gst-plugins-0.8.6-faad2-test.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	%{gstreamer}-devel >= %{gst_minver}
# libtool needs this, sigh
BuildRequires:	gcc-c++
# so gst-libs can build
BuildRequires:	XFree86-devel

# so configure passes
BuildRequires:	GConf2-devel

# because we patch configure.in
BuildRequires:	autoconf, automake, libtool, gettext-devel, which, cvs

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package audio
Summary:	Extra audio plugins for GStreamer
Group:		Applications/Multimedia

BuildRequires:	faad2-devel >= 2.0
BuildRequires:	gsm-devel >= 1.0.10
BuildRequires:	lame-devel >= 3.89
BuildRequires:	libid3tag-devel >= 0.15.0
BuildRequires:	libmad-devel >= 0.15.0
BuildRequires:	libmusepack-devel

Requires:	%{gstreamer}-plugins >= %{gstp_minver}
Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}

Provides:	%{gstreamer}-faad = %{version}-%{release}
Provides:	%{gstreamer}-gsm = %{version}-%{release}
Provides:	%{gstreamer}-lame = %{version}-%{release}
Provides:	%{gstreamer}-mad = %{version}-%{release}
Provides:	%{gstreamer}-musepack = %{version}-%{release}

%description audio
This package contains extra audio plugins for GStreamer, including
- gsm decoding
- faad2 decoding
- mad mp3 decoding
- lame mp3 encoding
- musepack mp3 decoding

%post audio
%{register}
%postun audio
%{register}

%files audio
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so

%package dvd
Summary:	DVD plugins for GStreamer
Group:		Applications/Multimedia

BuildRequires:	a52dec-devel >= 0.7.3
BuildRequires:	libdvdnav-devel >= 0.1.3
BuildRequires:	libdvdread-devel >= 0.9.0

Requires:	%{gstreamer}-plugins >= %{gstp_minver}
Requires:	%{gstreamer}-plugins-extra-video >= %{gstp_minver}
Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}

Provides:	%{gstreamer}-dvd = %{version}-%{release}
Provides:	%{gstreamer}-a52dec = %{version}-%{release}
Provides:	%{gstreamer}-dvdnavsrc = %{version}-%{release}
Provides:	%{gstreamer}-dvdreadsrc = %{version}-%{release}

%description dvd
This package contains dvd plugins for GStreamer, including
- libdvdnav
- libdvdread
- a52 decoding

%post dvd
%{register}
%postun dvd
%{register}

%files dvd
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdnavsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdreadsrc.so

%package video
Summary:	Extra video plugins for GStreamer
Group:		Applications/Multimedia

BuildRequires:	libfame-devel >= 0.9.1
BuildRequires:	mpeg2dec-devel >= 0.4.0
BuildRequires:	swfdec-devel >= 0.3.1

Requires:	%{gstreamer}-plugins >= %{gstp_minver}
Requires:	%{gstreamer}-plugins-extra-audio >= %{gstp_minver}
Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}

Provides:	%{gstreamer}-libfame = %{version}-%{release}
Provides:	%{gstreamer}-mpeg2dec = %{version}-%{release}
Provides:	%{gstreamer}-swfdec = %{version}-%{release}

%description video
This package contains extra video plugins for GStreamer, including
- libfame MPEG video encoding
- mpeg2dec MPEG-2 decoding
- swfdec Flash decoding

%post video
%{register}
%postun video
%{register}

%files video
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstlibfame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstmp1videoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg1systemencode.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2subt.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudioparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegstream.so
%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so

%prep
%setup -n gst-plugins-%{version}
%patch -p1 -b .faad2

%build
./autogen.sh --noconfigure
%configure \
  --with-package-name='Fedora freshrpms rpm' \
  --with-package-origin='http://freshrpms.net/' \
  --with-plugins=\
mpeg1sys,mpeg1videoparse,mpeg2sub,mpegaudio,mpegaudioparse,mpegstream \
  --enable-debug \
  --enable-DEBUG \
  --disable-tests \
  --disable-examples

# Die if some of the plugins we want aren't configured properly
grep -oP "(?<=will not be built: )[[:alpha:] ]+" config.log | sort > notbuilt
BADPLUGS=$(echo %{gstplugs} %{extplugs} | xargs -n1 echo | sort | join - notbuilt)
if [ $BADPLUGS != "" ]; then
	echo "Plugins not configured: $BADPLUGS"
	exit 1;
fi

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# we're better off manually installing the plugins we want to package

cd gst
for p in %{gstplugs}
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

cd ext
for p in %{extplugs}
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb  2 2005 Matthias Saou <http://freshrpms.net/> 0.8.6-1
- Include all changes by Nicholas Miell :
- Fix for faad2 detection (new and old).
- Have build die if any of the requested plugins aren't configured properly,
  since they could get built (because of the short circuiting of the built)
  but be totally broken.

* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 0.8.6-0
- Update to 0.8.6.
- Sync with Thomas's current spec file.

* Mon Nov 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5.3-0.lvn.1
- new prerelease

* Wed Oct 06 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5-0.lvn.1: new release
- added GConf2 requirement to pass configure

* Tue Aug 31 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.4-0.lvn.1: new release

* Fri Aug 27 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3.2-0.lvn.1: new prerelease

* Mon Aug 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3-0.lvn.1: new source release

* Fri Jul 30 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.2.2-0.lvn.1: new prerelease

* Wed Jun 23 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.2-0.lvn.1: new source release

* Fri Jun 18 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1.2-0.lvn.1: new source prerelease

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.lvn.1: new source release

* Tue Mar 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: new source release, change base name to gstreamer

* Tue Mar 09 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.6-0.lvn.1: new source release

* Fri Mar 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.lvn.2: sync with FreshRPMS

* Tue Mar 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.lvn.1: First package for rpm.livna.org
