# $NetBSD$

DISTNAME=	typer-0.20.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=t/typer/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/typer/
COMMENT=	Typer is a library for building CLI applications
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-flit_core>=2.0:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-click>=7.1.1:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=3.7.4.3:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-pdm>=0:../../devel/py-pdm

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} typer typer-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
