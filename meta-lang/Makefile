# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-lang-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs lang shells python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for programming languages
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# shells
DEPENDS+=	tcsh>=0:../../shells/tcsh
DEPENDS+=	zsh>=0:../../shells/zsh

# lang
DEPENDS+=	gawk>=0:../../lang/gawk
DEPENDS+=	gcc14>=0:../../lang/gcc14
DEPENDS+=	gcc13>=0:../../lang/gcc13
DEPENDS+=	gcc12>=0:../../lang/gcc12
DEPENDS+=	gcc10>=0:../../lang/gcc10
DEPENDS+=	gcc9>=0:../../lang/gcc9
DEPENDS+=	gcc8>=0:../../lang/gcc8
DEPENDS+=	gcc7>=0:../../lang/gcc7
DEPENDS+=	gcc6>=0:../../lang/gcc6
DEPENDS+=	gcc2>=0:../../lang/gcc2
DEPENDS+=	perl>=0:../../lang/perl5
DEPENDS+=	python313>=0:../../lang/python313
DEPENDS+=	python312>=0:../../lang/python312
DEPENDS+=	python311>=0:../../lang/python311
DEPENDS+=	python310>=0:../../lang/python310
DEPENDS+=	python39>=0:../../lang/python39
DEPENDS+=	python27>=0:../../lang/python27
DEPENDS+=	rust>=0:../../lang/rust
DEPENDS+=	tcl>=0:../../lang/tcl

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
