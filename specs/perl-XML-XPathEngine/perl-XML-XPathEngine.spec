# $Id$
# Authority: dries
# Upstream: Michel Rodriguez <mirod$xmltwig,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-XPathEngine

Summary: Reusable XPath engine for DOM-like trees
Name: perl-XML-XPathEngine
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-XPathEngine/

Source: http://search.cpan.org//CPAN/authors/id/M/MI/MIROD/XML-XPathEngine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is used to add XPath support to XML modules.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/XPathEngine.pm
%{perl_vendorlib}/XML/XPathEngine/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
