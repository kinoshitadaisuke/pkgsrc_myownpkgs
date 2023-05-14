# $NetBSD$

DISTNAME=	ephem-4.1.4
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=e/ephem/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/ephem/
COMMENT=	High-precision ephemeris computations for astronomy
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-docutils>=0.17.1:../../textproc/py-docutils
DEPENDS+=	${PYPKGPREFIX}-sphinx>=1.7.6:../../textproc/py-sphinx

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
