# $NetBSD$

DISTNAME=	modin-0.37.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=m/modin/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/modin/
COMMENT=	drop-in replacement for pandas
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-pandas>=2.2:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.22.4:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-fsspec>=2022.11.0:../../sysutils/py-fsspec
DEPENDS+=	${PYPKGPREFIX}-packaging>=21.0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-psutil>=5.8.0:../../sysutils/py-psutil

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
